; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "HelpCom"
#define MyAppVersion "1.0"
#define MyAppPublisher "Elvin Bağırov"
#define MyAppURL "ww.elba.com"
#define MyAppExeName "yeni.exe"
#define MyAppAssocName MyAppName + " File"
#define MyAppAssocExt ".myp"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{B7A871BB-B431-4D5D-BA4A-205586BD2F6B}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
ChangesAssociations=yes
DisableProgramGroupPage=yes
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=Installer
OutputBaseFilename=HelpCom.exe
SetupIconFile=C:\Users\Tarana.Ismayilova\Desktop\Elvin\el.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\HelpCom\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\add.PNG"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\bolge.PNG"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\comp.PNG"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\directX.PNG"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\disksil.PNG"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\ekran.PNG"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\enerji.PNG"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\FOLDER.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\hardware.PNG"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\int.PNG"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\internet_parametrleri.PNG"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\kilit.PNG"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\ox.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\qurgu.PNG"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\restart.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\saat.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\ses.PNG"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\shutdown.PNG"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\sistem.PNG"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\tapsiriq.PNG"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Tarana.Ismayilova\Desktop\Elvin\el.ico"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocExt}\OpenWithProgids"; ValueType: string; ValueName: "{#MyAppAssocKey}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}"; ValueType: string; ValueName: ""; ValueData: "{#MyAppAssocName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""
Root: HKA; Subkey: "Software\Classes\Applications\{#MyAppExeName}\SupportedTypes"; ValueType: string; ValueName: ".myp"; ValueData: ""

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

