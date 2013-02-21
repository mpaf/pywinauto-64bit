from pywinauto.application import Application as A
import time

a = A.start(r"c:\_temp\winzip120.exe")
a.WinzipSetup.Info.Click()
a.WinzipSelfExtractor.OK.Click()
a.WinzipSetup.Setup.Click()

# wait for the next window to open
time.sleep(2)

a2 = A()
a2.connect(title_re = "WinZip Setup - Uniblue.*")
a2.WinZipSetupUniblueRegistryBoosterOffer.NoThaknsPleaseJustInstallWinzip.Click()
a2.WinZipSetupUniblueRegistryBoosterOffer.Continue.Click()

# wait for the next window to open
time.sleep(2)

a3 = A()
a3.Connect(title = "WinZip 12.0 Setup")
a3.Winzip120Setup.DrawOutline()
a3.Winzip120Setup.Next.Click()
a3.Winzip120Setup.IAcceptTheLicense.Click()
a3.Winzip120Setup.Next.Click()
a3.Winzip120Setup.Next.Click()


a3.Winzip120Setup.Next.Click()
a3.Winzip120Setup.Window_(title = "Click Next to begin installation.").Wait("Exists", 10)


a3.Winzip120Setup.Cancel.Click()
a3.Winzip120Setup.ExitSetup.Click()
a3.Winzip120SetupCancelled.OK.Click()


