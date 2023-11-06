# Windows-Setup-Usages

## Install - Configuration

### Install

 1. Setup Chocolatey

### Configuration

#### Config-Powershell

```sh
 Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted  # AllSigned|RemoteSigned|Unrestricted|Restricted
```

## Usages

### CLI Tools

#### CLI-Terminal

#### CLI-Powershell

* [Execution Policies](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.3)

```sh
 Get-ExecutionPolicy  # Get execution (Default: -Scope CurrentUser)
 Get-ExecutionPolicy -List  # Get execution lists (MachinePolicy|UserPolicy|Process|LocalMachine)
 Get-History  # Get all 
 Get-Childitem -Path Env:* | Sort-Object Name  # Get all $env:<
 Get-Command -Name Python # Get command in powershell
```

## Guideline

### Chocolatey

* [Choco install](https://docs.chocolatey.org/en-us/choco/setup#more-install-options)

#### Chocolatey-install

1. First, ensure that you are using an administrative shell.
   * Refer to Non-Administrative Installation for information on installing without administrative rights.
2. Copy the text specific to your command shell - cmd.exe or powershell.exe.
3. Paste the copied text into your shell and press Enter.
4. Wait a few seconds for the command to complete.
5. If you don't see any errors, you are ready to use Chocolatey CLI!
6. Type choco or choco -? now, or see Getting Started for usage instructions.

Install with cmd.exe

```batch
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```

Install with PowerShell.exe

```batch
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
