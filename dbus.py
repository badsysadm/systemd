from pydbus import SystemBus
#from serial import Serial

bus = SystemBus()
systemd = bus.get(
    '.systemd1'
)
print(systemd.UnitPath)
print(systemd.Version)
print(systemd.Features)
print(systemd.LogTarget)
print(systemd.NNames)
print(systemd.NJobs)
print(systemd.NInstalledJobs)
print(systemd.NFailedJobs)
print(systemd.Environment)
print(systemd.Progress)
print(systemd.DefaultStandardOutput)
print(systemd.DefaultStandardError)
print(systemd.Virtualization)
print(systemd.Architecture)
print(systemd.ControlGroup)
#ControlGroup contains the root control group path of this system manager. Note that the root path is encoded as empty string here (not as "/"!), so that it can be appended to /sys/fs/cgroup/systemd easily. This value will be set to the empty string for the host instance, and some other string for container instances.

unit = systemd.GetUnit('systemd-nspawn@gentoo.service')
#Start
#Stop
#Reload
#Restart
#Kill
#ResetFailed

systemd_unit = bus.get(
    '.systemd1',
    unit
)
print(systemd_unit.Id)
print(systemd_unit.Names)
print(systemd_unit.Following)
print(systemd_unit.Requires)
print(systemd_unit.Wants)
print(systemd_unit.BindsTo)
print(systemd_unit.PartOf)
print(systemd_unit.Requisite)
print(systemd_unit.RequiredBy)
print(systemd_unit.WantedBy)
print(systemd_unit.BoundBy)
print(systemd_unit.ConsistsOf)
print(systemd_unit.ConflictedBy)
print(systemd_unit.After)
print(systemd_unit.Before)
print(systemd_unit.OnFailure)
print(systemd_unit.Triggers)
print(systemd_unit.TriggeredBy)
print(systemd_unit.RequiresMountsFor)

print(systemd_unit.Description)
print(systemd_unit.SourcePath)
print(systemd_unit.Documentation)
print(systemd_unit.LoadState)
print(systemd_unit.ActiveState)
print(systemd_unit.SubState)
print(systemd_unit.FragmentPath)
print(systemd_unit.UnitFileState)
print(systemd_unit.InactiveExitTimestamp)
print(systemd_unit.ActiveEnterTimestamp)
print(systemd_unit.ActiveExitTimestamp)
print(systemd_unit.InactiveEnterTimestamp)
print(systemd_unit.CanStart)
print(systemd_unit.CanStop)
print(systemd_unit.CanReload)
print(systemd_unit.CanIsolate)
print(systemd_unit.NeedDaemonReload)
print(systemd_unit.ConditionTimestamp)
print(systemd_unit.Conditions)
print(systemd_unit.Transient)


unit = systemd.GetUnit('init.scope')

systemd_unit = bus.get(
    '.systemd1',
    unit
)
print(systemd_unit.Id)
print(systemd_unit.Slice)
print(systemd_unit.ControlGroup)
print(systemd_unit.CPUAccounting)
print(systemd_unit.CPUShares)
print(systemd_unit.BlockIOAccounting)
print(systemd_unit.BlockIOWeight)
print(systemd_unit.BlockIODeviceWeight)
print(systemd_unit.BlockIOReadBandwidth)
print(systemd_unit.BlockIOWriteBandwidth)
print(systemd_unit.MemoryAccounting)
print(systemd_unit.MemoryLimit)
print(systemd_unit.DevicePolicy)
print(systemd_unit.DeviceAllow)
print(systemd_unit.Result)
print(systemd_unit.Controller)

unit = systemd.GetUnit(systemd_unit.Slice)
systemd_unit = bus.get(
    '.systemd1',
    unit
)
print(systemd_unit.Id)
print(systemd_unit.Slice)
print(systemd_unit.ControlGroup)
print(systemd_unit.CPUAccounting)
print(systemd_unit.CPUShares)
print(systemd_unit.BlockIOAccounting)
print(systemd_unit.BlockIOWeight)
print(systemd_unit.BlockIODeviceWeight)
print(systemd_unit.BlockIOReadBandwidth)
print(systemd_unit.BlockIOWriteBandwidth)
print(systemd_unit.MemoryAccounting)
print(systemd_unit.MemoryLimit)
print(systemd_unit.DevicePolicy)
print(systemd_unit.DeviceAllow)
