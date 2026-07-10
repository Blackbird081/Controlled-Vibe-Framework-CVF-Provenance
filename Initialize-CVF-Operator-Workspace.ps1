<#
.SYNOPSIS
    Interactive fresh-clone entrypoint for creating or refreshing a CVF Workspace.

.DESCRIPTION
    Run this file from a trusted CVF provenance clone. With no arguments it
    shows profile options, asks for the workspace path, confirms the plan, and
    creates or refreshes the workspace. Agents may use the non-interactive
    parameters after the operator has selected a path and profile.
#>

param(
    [string]$WorkspaceRoot = "",

    [ValidateSet("", "public-free", "paid-user-safe", "operator-local")]
    [string]$ProfileName = "",

    [ValidateSet("", "Create", "Check", "Update")]
    [string]$Action = "",

    [switch]$NonInteractive,

    [switch]$Gui,

    [switch]$GuiSmokeTest,

    [switch]$PlanOnly,

    [switch]$SkipEnforcementGate
)

$ErrorActionPreference = "Stop"
$publicRemote = "https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git"
$provenanceRemote = "https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF-Provenance.git"
$provenanceRoot = [System.IO.Path]::GetFullPath($PSScriptRoot)
$interactive = -not $NonInteractive -and -not $Gui -and -not $GuiSmokeTest

function Write-Step([string]$Message) {
    Write-Host "[STEP] $Message" -ForegroundColor Cyan
}

function Write-Ok([string]$Message) {
    Write-Host "[OK]   $Message" -ForegroundColor Green
}

function Invoke-CheckedPowerShell {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ScriptPath,

        [string[]]$Arguments = @()
    )

    & powershell -NoProfile -ExecutionPolicy Bypass -File $ScriptPath @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Command failed with exit code $LASTEXITCODE`: $ScriptPath"
    }
}

function Select-WorkspaceProfile {
    Write-Host ""
    Write-Host "CVF Workspace Setup" -ForegroundColor Cyan
    Write-Host "===================" -ForegroundColor Cyan
    Write-Host "1. operator-local   Recommended for the private operator machine"
    Write-Host "2. paid-user-safe   Shared team or future paid-user workspace"
    Write-Host "3. public-free      Lightest public-safe workspace"
    Write-Host "4. Cancel"
    Write-Host ""

    while ($true) {
        $choice = Read-Host "Select profile [1-4]"
        switch ($choice) {
            "1" { return "operator-local" }
            "2" { return "paid-user-safe" }
            "3" { return "public-free" }
            "4" { return "" }
            default { Write-Host "Enter 1, 2, 3, or 4." -ForegroundColor Yellow }
        }
    }
}

function Show-WorkspaceSetupWizard {
    param(
        [string]$DefaultWorkspace,
        [switch]$SmokeTest
    )

    Add-Type -AssemblyName System.Windows.Forms
    Add-Type -AssemblyName System.Drawing
    [System.Windows.Forms.Application]::EnableVisualStyles()

    $form = New-Object System.Windows.Forms.Form
    $form.Text = "CVF Workspace Setup"
    $form.StartPosition = "CenterScreen"
    $form.FormBorderStyle = "FixedDialog"
    $form.MaximizeBox = $false
    $form.MinimizeBox = $false
    $form.ClientSize = New-Object System.Drawing.Size(640, 410)
    $form.Font = New-Object System.Drawing.Font("Segoe UI", 10)

    $title = New-Object System.Windows.Forms.Label
    $title.Location = New-Object System.Drawing.Point(28, 20)
    $title.Size = New-Object System.Drawing.Size(580, 34)
    $title.Font = New-Object System.Drawing.Font("Segoe UI Semibold", 17)
    $title.Text = "Check, update, or create a CVF Workspace"
    $form.Controls.Add($title)

    $stepLabel = New-Object System.Windows.Forms.Label
    $stepLabel.Location = New-Object System.Drawing.Point(31, 60)
    $stepLabel.Size = New-Object System.Drawing.Size(560, 24)
    $stepLabel.ForeColor = [System.Drawing.Color]::FromArgb(80, 80, 80)
    $form.Controls.Add($stepLabel)

    $content = New-Object System.Windows.Forms.Panel
    $content.Location = New-Object System.Drawing.Point(28, 92)
    $content.Size = New-Object System.Drawing.Size(584, 245)
    $form.Controls.Add($content)

    $profilePage = New-Object System.Windows.Forms.Panel
    $profilePage.Dock = "Fill"
    $content.Controls.Add($profilePage)

    $actionLabel = New-Object System.Windows.Forms.Label
    $actionLabel.Location = New-Object System.Drawing.Point(0, 0)
    $actionLabel.Size = New-Object System.Drawing.Size(150, 28)
    $actionLabel.Text = "Action"
    $actionLabel.Font = New-Object System.Drawing.Font("Segoe UI Semibold", 11)
    $profilePage.Controls.Add($actionLabel)

    $actionBox = New-Object System.Windows.Forms.ComboBox
    $actionBox.Location = New-Object System.Drawing.Point(160, 0)
    $actionBox.Size = New-Object System.Drawing.Size(405, 30)
    $actionBox.DropDownStyle = "DropDownList"
    [void]$actionBox.Items.Add("Check status and available updates (recommended)")
    [void]$actionBox.Items.Add("Update an existing workspace")
    [void]$actionBox.Items.Add("Create a new workspace")
    $actionBox.SelectedIndex = 0
    $profilePage.Controls.Add($actionBox)

    $profilePrompt = New-Object System.Windows.Forms.Label
    $profilePrompt.Location = New-Object System.Drawing.Point(0, 48)
    $profilePrompt.Size = New-Object System.Drawing.Size(560, 28)
    $profilePrompt.Text = "Profile (choose only when creating)"
    $profilePrompt.Font = New-Object System.Drawing.Font("Segoe UI Semibold", 11)
    $profilePage.Controls.Add($profilePrompt)

    $operatorRadio = New-Object System.Windows.Forms.RadioButton
    $operatorRadio.Location = New-Object System.Drawing.Point(8, 82)
    $operatorRadio.Size = New-Object System.Drawing.Size(550, 32)
    $operatorRadio.Text = "operator-local - private operator machine (recommended)"
    $operatorRadio.Checked = $true
    $profilePage.Controls.Add($operatorRadio)

    $paidRadio = New-Object System.Windows.Forms.RadioButton
    $paidRadio.Location = New-Object System.Drawing.Point(8, 120)
    $paidRadio.Size = New-Object System.Drawing.Size(550, 32)
    $paidRadio.Text = "paid-user-safe - shared team or future paid-user workspace"
    $profilePage.Controls.Add($paidRadio)

    $publicRadio = New-Object System.Windows.Forms.RadioButton
    $publicRadio.Location = New-Object System.Drawing.Point(8, 158)
    $publicRadio.Size = New-Object System.Drawing.Size(550, 32)
    $publicRadio.Text = "public-free - lightest public-safe workspace"
    $profilePage.Controls.Add($publicRadio)

    $profileNote = New-Object System.Windows.Forms.Label
    $profileNote.Location = New-Object System.Drawing.Point(8, 202)
    $profileNote.Size = New-Object System.Drawing.Size(550, 38)
    $profileNote.Text = "Private continuity is available only in operator-local. Do not use it for a customer or public workspace."
    $profileNote.ForeColor = [System.Drawing.Color]::FromArgb(90, 90, 90)
    $profilePage.Controls.Add($profileNote)

    $setProfileSelectionState = {
        $canSelectProfile = ($actionBox.SelectedIndex -eq 2)
        $operatorRadio.Enabled = $canSelectProfile
        $paidRadio.Enabled = $canSelectProfile
        $publicRadio.Enabled = $canSelectProfile
        $profileNote.Text = if ($canSelectProfile) {
            "Choose the smallest profile that fits the workspace audience."
        }
        else {
            "The active profile will be detected and preserved for this existing workspace."
        }
    }
    $actionBox.Add_SelectedIndexChanged($setProfileSelectionState)
    & $setProfileSelectionState

    $pathPage = New-Object System.Windows.Forms.Panel
    $pathPage.Dock = "Fill"
    $pathPage.Visible = $false
    $content.Controls.Add($pathPage)

    $pathPrompt = New-Object System.Windows.Forms.Label
    $pathPrompt.Location = New-Object System.Drawing.Point(0, 0)
    $pathPrompt.Size = New-Object System.Drawing.Size(560, 28)
    $pathPrompt.Text = "Choose the workspace folder"
    $pathPrompt.Font = New-Object System.Drawing.Font("Segoe UI Semibold", 11)
    $pathPage.Controls.Add($pathPrompt)

    $pathBox = New-Object System.Windows.Forms.TextBox
    $pathBox.Location = New-Object System.Drawing.Point(4, 48)
    $pathBox.Size = New-Object System.Drawing.Size(455, 30)
    $pathBox.Text = $DefaultWorkspace
    $pathPage.Controls.Add($pathBox)

    $browseButton = New-Object System.Windows.Forms.Button
    $browseButton.Location = New-Object System.Drawing.Point(470, 46)
    $browseButton.Size = New-Object System.Drawing.Size(105, 32)
    $browseButton.Text = "Browse..."
    $pathPage.Controls.Add($browseButton)

    $pathNote = New-Object System.Windows.Forms.Label
    $pathNote.Location = New-Object System.Drawing.Point(4, 96)
    $pathNote.Size = New-Object System.Drawing.Size(560, 80)
    $pathNote.Text = "For a new workspace, select an empty folder. For refresh, select an existing CVF Workspace containing .Controlled-Vibe-Framework-CVF. The workspace root must not be a git repository."
    $pathNote.ForeColor = [System.Drawing.Color]::FromArgb(90, 90, 90)
    $pathPage.Controls.Add($pathNote)

    $summaryPage = New-Object System.Windows.Forms.Panel
    $summaryPage.Dock = "Fill"
    $summaryPage.Visible = $false
    $content.Controls.Add($summaryPage)

    $summaryPrompt = New-Object System.Windows.Forms.Label
    $summaryPrompt.Location = New-Object System.Drawing.Point(0, 0)
    $summaryPrompt.Size = New-Object System.Drawing.Size(560, 28)
    $summaryPrompt.Text = "Review and confirm"
    $summaryPrompt.Font = New-Object System.Drawing.Font("Segoe UI Semibold", 11)
    $summaryPage.Controls.Add($summaryPrompt)

    $summaryText = New-Object System.Windows.Forms.TextBox
    $summaryText.Location = New-Object System.Drawing.Point(4, 42)
    $summaryText.Size = New-Object System.Drawing.Size(570, 145)
    $summaryText.Multiline = $true
    $summaryText.ReadOnly = $true
    $summaryText.BackColor = [System.Drawing.Color]::White
    $summaryPage.Controls.Add($summaryText)

    $summaryNote = New-Object System.Windows.Forms.Label
    $summaryNote.Location = New-Object System.Drawing.Point(4, 198)
    $summaryNote.Size = New-Object System.Drawing.Size(560, 40)
    $summaryNote.Text = "Setup verifies remotes, profile boundaries, required files, and workspace enforcement."
    $summaryPage.Controls.Add($summaryNote)

    $backButton = New-Object System.Windows.Forms.Button
    $backButton.Location = New-Object System.Drawing.Point(332, 354)
    $backButton.Size = New-Object System.Drawing.Size(86, 34)
    $backButton.Text = "< Back"
    $backButton.Enabled = $false
    $form.Controls.Add($backButton)

    $nextButton = New-Object System.Windows.Forms.Button
    $nextButton.Location = New-Object System.Drawing.Point(426, 354)
    $nextButton.Size = New-Object System.Drawing.Size(92, 34)
    $nextButton.Text = "Next >"
    $form.Controls.Add($nextButton)
    $form.AcceptButton = $nextButton

    $cancelButton = New-Object System.Windows.Forms.Button
    $cancelButton.Location = New-Object System.Drawing.Point(526, 354)
    $cancelButton.Size = New-Object System.Drawing.Size(86, 34)
    $cancelButton.Text = "Cancel"
    $cancelButton.DialogResult = [System.Windows.Forms.DialogResult]::Cancel
    $form.Controls.Add($cancelButton)
    $form.CancelButton = $cancelButton

    $state = @{
        Page = 0
        Action = "Check"
        ProfileName = "operator-local"
        WorkspaceRoot = $DefaultWorkspace
    }
    $pages = @($profilePage, $pathPage, $summaryPage)

    $showPage = {
        param([int]$Index)
        $state.Page = $Index
        for ($i = 0; $i -lt $pages.Count; $i++) {
            $pages[$i].Visible = ($i -eq $Index)
        }
        $stepLabel.Text = "Step $($Index + 1) of 3"
        $backButton.Enabled = ($Index -gt 0)
        $nextButton.Text = if ($Index -eq 2) {
            switch ($state.Action) {
                "Check" { "Check" }
                "Update" { "Update" }
                default { "Create" }
            }
        }
        else {
            "Next >"
        }
    }

    $browseButton.Add_Click({
        $dialog = New-Object System.Windows.Forms.FolderBrowserDialog
        $dialog.Description = "Choose a new empty folder or an existing CVF Workspace"
        $dialog.SelectedPath = $pathBox.Text
        if ($dialog.ShowDialog($form) -eq [System.Windows.Forms.DialogResult]::OK) {
            $pathBox.Text = $dialog.SelectedPath
        }
        $dialog.Dispose()
    })

    $backButton.Add_Click({
        if ($state.Page -gt 0) {
            & $showPage ($state.Page - 1)
        }
    })

    $nextButton.Add_Click({
        if ($state.Page -eq 0) {
            $state.Action = @("Check", "Update", "Create")[$actionBox.SelectedIndex]
            $state.ProfileName = if ($operatorRadio.Checked) {
                "operator-local"
            }
            elseif ($paidRadio.Checked) {
                "paid-user-safe"
            }
            else {
                "public-free"
            }
            & $showPage 1
            return
        }

        if ($state.Page -eq 1) {
            if ([string]::IsNullOrWhiteSpace($pathBox.Text)) {
                [System.Windows.Forms.MessageBox]::Show(
                    $form,
                    "Choose a workspace folder before continuing.",
                    "CVF Workspace Setup",
                    [System.Windows.Forms.MessageBoxButtons]::OK,
                    [System.Windows.Forms.MessageBoxIcon]::Warning
                ) | Out-Null
                return
            }
            try {
                $state.WorkspaceRoot = [System.IO.Path]::GetFullPath($pathBox.Text)
            }
            catch {
                [System.Windows.Forms.MessageBox]::Show(
                    $form,
                    "The workspace path is invalid.",
                    "CVF Workspace Setup",
                    [System.Windows.Forms.MessageBoxButtons]::OK,
                    [System.Windows.Forms.MessageBoxIcon]::Warning
                ) | Out-Null
                return
            }
            if ($state.Action -ne "Create") {
                $activeForPath = Get-ActiveProfile -Path $state.WorkspaceRoot
                if ($null -ne $activeForPath) {
                    $state.ProfileName = $activeForPath.activeProfile
                }
            }
            $summaryText.Text = "Action:`r`n  $($state.Action)`r`n`r`nProfile:`r`n  $($state.ProfileName)`r`n`r`nWorkspace:`r`n  $($state.WorkspaceRoot)"
            & $showPage 2
            return
        }

        $form.Tag = [pscustomobject]@{
            Action = $state.Action
            ProfileName = $state.ProfileName
            WorkspaceRoot = $state.WorkspaceRoot
        }
        $form.DialogResult = [System.Windows.Forms.DialogResult]::OK
        $form.Close()
    })

    & $showPage 0

    if ($SmokeTest) {
        $timer = New-Object System.Windows.Forms.Timer
        $timer.Interval = 600
        $timer.Add_Tick({
            $timer.Stop()
            $form.Tag = [pscustomobject]@{
                Action = "Check"
                ProfileName = "operator-local"
                WorkspaceRoot = $DefaultWorkspace
            }
            $form.DialogResult = [System.Windows.Forms.DialogResult]::OK
            $form.Close()
        })
        $timer.Start()
    }

    $result = $form.ShowDialog()
    $selection = $form.Tag
    $form.Dispose()
    if ($result -ne [System.Windows.Forms.DialogResult]::OK) {
        return $null
    }
    return $selection
}
function Assert-Prerequisites {
    foreach ($command in @("git", "powershell")) {
        if (-not (Get-Command $command -ErrorAction SilentlyContinue)) {
            throw "Required command is not available in PATH: $command"
        }
    }

    if (-not (Test-Path -LiteralPath (Join-Path $provenanceRoot ".git") -PathType Container)) {
        throw "Run this file from a cloned CVF provenance repository."
    }

    $remote = (git -C $provenanceRoot remote get-url origin 2>$null).Trim()
    if ($LASTEXITCODE -ne 0 -or $remote -ne $provenanceRemote) {
        throw "Provenance origin mismatch. Expected: $provenanceRemote; found: $remote"
    }

    foreach ($relativePath in @(
        "scripts\install_cvf_workspace.ps1",
        "scripts\install_cvf_workspace_root_wrappers_public.ps1",
        "scripts\sync_cvf_workspace_rule_pack.ps1"
    )) {
        $path = Join-Path $provenanceRoot $relativePath
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
            throw "Required workspace source is missing: $path"
        }
    }
}

function Assert-WorkspaceBoundary([string]$Path) {
    if (Test-Path -LiteralPath (Join-Path $Path ".git") -PathType Container) {
        throw "Workspace root must not be a git repository: $Path"
    }

    if ($Path.TrimEnd("\") -eq $provenanceRoot.TrimEnd("\")) {
        throw "Workspace root must be separate from the provenance repository."
    }
}

function Get-ActiveProfile([string]$Path) {
    $activePath = Join-Path $Path "CVF_RULE_PACKS\ACTIVE_RULE_PACK.json"
    if (-not (Test-Path -LiteralPath $activePath -PathType Leaf)) {
        return $null
    }
    return (Get-Content -LiteralPath $activePath -Raw -Encoding utf8 | ConvertFrom-Json)
}

function Install-NewWorkspace([string]$Path, [string]$Profile) {
    $baseProfile = $Profile
    if ($Profile -eq "operator-local") {
        $baseProfile = "paid-user-safe"
    }

    Write-Step "Installing hidden public core and '$baseProfile' base profile"
    Invoke-CheckedPowerShell `
        -ScriptPath (Join-Path $provenanceRoot "scripts\install_cvf_workspace.ps1") `
        -Arguments @("-WorkspaceRoot", $Path, "-ProfileName", $baseProfile)

    Write-Step "Aligning root wrappers and guides with the trusted provenance clone"
    Invoke-CheckedPowerShell `
        -ScriptPath (Join-Path $provenanceRoot "scripts\install_cvf_workspace_root_wrappers_public.ps1") `
        -Arguments @("-WorkspaceRoot", $Path)
}

function Update-ProvenanceSource {
    if (@(git -C $provenanceRoot status --porcelain).Count -gt 0) {
        throw "Provenance clone is dirty. Commit, discard, or move those changes before updating workspace sources."
    }
    Write-Step "Fast-forwarding the provenance source"
    git -C $provenanceRoot pull --ff-only
    if ($LASTEXITCODE -ne 0) {
        throw "Provenance fast-forward failed."
    }
}

function Refresh-ExistingWorkspace([string]$Path) {
    $corePath = Join-Path $Path ".Controlled-Vibe-Framework-CVF"
    if (-not (Test-Path -LiteralPath $corePath -PathType Container)) {
        throw "Workspace exists but hidden public core is missing: $corePath"
    }

    $remote = (git -C $corePath remote get-url origin 2>$null).Trim()
    if ($LASTEXITCODE -ne 0 -or $remote -ne $publicRemote) {
        throw "Hidden core origin mismatch. Expected: $publicRemote; found: $remote"
    }

    $dirty = @(git -C $corePath status --porcelain)
    if ($LASTEXITCODE -ne 0) {
        throw "Could not read hidden core status."
    }
    if ($dirty.Count -gt 0) {
        throw "Hidden public core is dirty. Review it before workspace refresh."
    }

    Write-Step "Fast-forwarding hidden public core"
    git -C $corePath pull --ff-only
    if ($LASTEXITCODE -ne 0) {
        throw "Hidden public core fast-forward failed."
    }

    Write-Step "Refreshing workspace root wrappers and guides"
    Invoke-CheckedPowerShell `
        -ScriptPath (Join-Path $provenanceRoot "scripts\install_cvf_workspace_root_wrappers_public.ps1") `
        -Arguments @("-WorkspaceRoot", $Path)
}

function Apply-SelectedProfile([string]$Path, [string]$Profile) {
    if ($Profile -eq "operator-local") {
        Write-Step "Applying private operator-local rule pack"
        Invoke-CheckedPowerShell `
            -ScriptPath (Join-Path $provenanceRoot "scripts\sync_cvf_workspace_rule_pack.ps1") `
            -Arguments @(
                "-WorkspaceRoot", $Path,
                "-ProfileName", "operator-local",
                "-AllowProvenanceContinuity"
            )
        return
    }

    $corePath = Join-Path $Path ".Controlled-Vibe-Framework-CVF"
    $profileScript = Join-Path $corePath "scripts\sync_cvf_workspace_public_profile.ps1"
    Write-Step "Applying public-safe '$Profile' profile"
    Invoke-CheckedPowerShell `
        -ScriptPath $profileScript `
        -Arguments @("-WorkspaceRoot", $Path, "-ProfileName", $Profile)
}

. (Join-Path $PSScriptRoot "scripts\\cvf_workspace_assessment.ps1")

try {
    Assert-Prerequisites

    $defaultWorkspace = Join-Path (Split-Path -Parent $provenanceRoot) "CVF-Workspace"

    if ($Gui -or $GuiSmokeTest) {
        $guiSelection = Show-WorkspaceSetupWizard `
            -DefaultWorkspace $defaultWorkspace `
            -SmokeTest:$GuiSmokeTest
        if ($null -eq $guiSelection) {
            exit 0
        }
        $Action = $guiSelection.Action
        $ProfileName = $guiSelection.ProfileName
        $WorkspaceRoot = $guiSelection.WorkspaceRoot
        if ($GuiSmokeTest) {
            Write-Ok "GUI wizard rendered and returned a valid selection"
            exit 0
        }
    }

    if ([string]::IsNullOrWhiteSpace($ProfileName)) {
        if (-not $interactive -and $Action -notin @("Check", "Update")) {
            throw "-ProfileName is required with -NonInteractive."
        }
        if ($interactive) {
            $ProfileName = Select-WorkspaceProfile
            if ([string]::IsNullOrWhiteSpace($ProfileName)) {
                Write-Host "Setup cancelled." -ForegroundColor Yellow
                exit 0
            }
        }
    }

    if ([string]::IsNullOrWhiteSpace($WorkspaceRoot)) {
        if (-not $interactive) {
            throw "-WorkspaceRoot is required with -NonInteractive."
        }
        $enteredPath = Read-Host "Workspace path [$defaultWorkspace]"
        if ([string]::IsNullOrWhiteSpace($enteredPath)) {
            $WorkspaceRoot = $defaultWorkspace
        }
        else {
            $WorkspaceRoot = $enteredPath
        }
    }

    $workspaceResolved = [System.IO.Path]::GetFullPath($WorkspaceRoot)
    Assert-WorkspaceBoundary -Path $workspaceResolved
    $coreExists = Test-Path -LiteralPath (Join-Path $workspaceResolved ".Controlled-Vibe-Framework-CVF") -PathType Container
    $activeBefore = Get-ActiveProfile -Path $workspaceResolved
    if ([string]::IsNullOrWhiteSpace($Action)) {
        $Action = if ($coreExists) { "Update" } else { "Create" }
    }
    if ($Action -eq "Create" -and $coreExists) {
        throw "Create requires a new target without a hidden public core. Choose Check or Update for this workspace."
    }
    if ($Action -in @("Check", "Update") -and -not $coreExists) {
        throw "$Action requires an existing CVF Workspace with a hidden public core."
    }
    if ([string]::IsNullOrWhiteSpace($ProfileName) -and $null -ne $activeBefore) {
        $ProfileName = $activeBefore.activeProfile
    }
    $operation = $Action.ToUpperInvariant()

    if (-not $coreExists -and (Test-Path -LiteralPath $workspaceResolved -PathType Container)) {
        $existingItems = @(Get-ChildItem -LiteralPath $workspaceResolved -Force)
        if ($existingItems.Count -gt 0) {
            throw "New workspace target is not empty. Select an empty folder or an existing CVF Workspace with a hidden public core."
        }
    }

    if (
        $null -ne $activeBefore -and
        $activeBefore.activeProfile -eq "operator-local" -and
        $ProfileName -ne "operator-local"
    ) {
        throw "Refusing to convert an operator-local workspace in place. Create a separate clean public or paid-user workspace."
    }

    Write-Host ""
    Write-Host "Setup plan" -ForegroundColor Cyan
    Write-Host "  Provenance: $provenanceRoot"
    Write-Host "  Workspace:  $workspaceResolved"
    Write-Host "  Profile:    $ProfileName"
    Write-Host "  Action:     $operation"
    Write-Host "  Boundary:   workspace root stays non-git; application projects stay outside hidden core"

    if ($PlanOnly) {
        Write-Ok "Plan validated; no files changed"
        exit 0
    }

    if ($interactive) {
        $confirmation = Read-Host "Continue? [Y/N]"
        if ($confirmation -notmatch "^(?i:y|yes)$") {
            Write-Host "Setup cancelled." -ForegroundColor Yellow
            exit 0
        }
    }

    if ($Action -eq "Check") {
        $assessment = Get-WorkspaceAssessment -Path $workspaceResolved
        Write-WorkspaceAssessment -Assessment $assessment
        if ($Gui) {
            Add-Type -AssemblyName System.Windows.Forms
            $detail = (@($assessment.Updates) + @($assessment.Issues)) -join "`r`n"
            if ([string]::IsNullOrWhiteSpace($detail)) { $detail = "No updates or repair issues found." }
            if ($assessment.Status -eq "UPDATE_AVAILABLE") {
                $decision = [System.Windows.Forms.MessageBox]::Show(
                    "Status: UPDATE_AVAILABLE`r`nProfile: $($assessment.Profile)`r`n`r`n$detail`r`n`r`nUpdate now?",
                    "CVF Workspace Check",
                    [System.Windows.Forms.MessageBoxButtons]::YesNo,
                    [System.Windows.Forms.MessageBoxIcon]::Question
                )
                if ($decision -eq [System.Windows.Forms.DialogResult]::Yes) {
                    $Action = "Update"
                }
                else { exit 0 }
            }
            else {
                [System.Windows.Forms.MessageBox]::Show(
                    "Status: $($assessment.Status)`r`nProfile: $($assessment.Profile)`r`n`r`n$detail",
                    "CVF Workspace Check",
                    [System.Windows.Forms.MessageBoxButtons]::OK,
                    [System.Windows.Forms.MessageBoxIcon]::Information
                ) | Out-Null
                exit 0
            }
        }
        else { exit $(if ($assessment.Status -eq "REPAIR_REQUIRED") { 1 } else { 0 }) }
    }

    Update-ProvenanceSource
    New-Item -ItemType Directory -Path $workspaceResolved -Force | Out-Null
    if ($Action -eq "Update") {
        Refresh-ExistingWorkspace -Path $workspaceResolved
    }
    else {
        Install-NewWorkspace -Path $workspaceResolved -Profile $ProfileName
    }

    Apply-SelectedProfile -Path $workspaceResolved -Profile $ProfileName
    Test-WorkspaceResult -Path $workspaceResolved -Profile $ProfileName
}
catch {
    Write-Host "[FAILED] $($_.Exception.Message)" -ForegroundColor Red
    if ($Gui -or $GuiSmokeTest) {
        Add-Type -AssemblyName System.Windows.Forms
        [System.Windows.Forms.MessageBox]::Show(
            $($_.Exception.Message),
            "CVF Workspace Setup Failed",
            [System.Windows.Forms.MessageBoxButtons]::OK,
            [System.Windows.Forms.MessageBoxIcon]::Error
        ) | Out-Null
    }
    elseif ($interactive) {
        [void](Read-Host "Press Enter to close")
    }
    exit 1
}

if ($Gui) {
    Add-Type -AssemblyName System.Windows.Forms
    [System.Windows.Forms.MessageBox]::Show(
        "CVF Workspace setup completed successfully.",
        "CVF Workspace Setup",
        [System.Windows.Forms.MessageBoxButtons]::OK,
        [System.Windows.Forms.MessageBoxIcon]::Information
    ) | Out-Null
}
elseif ($interactive) {
    [void](Read-Host "Press Enter to close")
}
