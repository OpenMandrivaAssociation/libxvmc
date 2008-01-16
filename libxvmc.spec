%define libxvmc %mklibname xvmc 1
Name: libxvmc
Summary:  The XvMC Library
Version: 1.0.4
Release: %mkrel 2
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXvMC-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros	>= 1.1.5
BuildRequires: libx11-devel	>= 1.1.3
BuildRequires: libxv-devel	>= 1.0.3
BuildRequires: x11-proto-devel	>= 7.3
BuildRequires: libxext-devel	>= 1.0.3

%description
The XvMC Library

#-----------------------------------------------------------

%package -n %{libxvmc}
Summary:  The XvMC Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxvmc}
The XvMC Library

#-----------------------------------------------------------

%package -n %{libxvmc}-devel
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libxvmc} = %{version}
Requires: libxv-devel >= 1.0.1
Requires: x11-proto-devel >= 1.0.0
Provides: libxvmc-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxvmc}-devel
Development files for %{name}

%pre -n %{libxvmc}-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libxvmc}-devel
%defattr(-,root,root)
%{_libdir}/libXvMCW.so
%{_libdir}/libXvMC.so
%{_libdir}/libXvMCW.la
%{_libdir}/libXvMC.la
%{_libdir}/pkgconfig/xvmc.pc
%{_includedir}/X11/extensions/XvMClib.h

#-----------------------------------------------------------

%package -n %{libxvmc}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxvmc}-devel >= %{version}
Provides: libxvmc-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxvmc}-static-devel
Static development files for %{name}

%files -n %{libxvmc}-static-devel
%defattr(-,root,root)
%{_libdir}/libXvMCW.a
%{_libdir}/libXvMC.a

#-----------------------------------------------------------

%prep
%setup -q -n libXvMC-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxvmc}
%defattr(-,root,root)
%{_libdir}/libXvMC.so.1
%{_libdir}/libXvMC.so.1.0.0
%{_libdir}/libXvMCW.so.1
%{_libdir}/libXvMCW.so.1.0.0
