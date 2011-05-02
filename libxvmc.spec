%define libname %mklibname xvmc 1
%define develname %mklibname xvmc -d
%define staticname %mklibname xvmc -s -d

Name: libxvmc
Summary:  The XvMC Library
Version: 1.0.6
Release: %mkrel 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXvMC-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxv-devel >= 1.0.1
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The XvMC Library

#-----------------------------------------------------------

%package -n %{libname}
Summary:  The XvMC Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
The XvMC Library

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libname} = %{version}-%{release}
Requires: libxv-devel >= 1.0.1
Requires: x11-proto-devel >= 1.0.0
Provides: libxvmc-devel = %{version}-%{release}
Provides: libxvmc1-devel = %{version}-%{release}
Obsoletes: %{mklibname xvmc 1 -d}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libXvMCW.so
%{_libdir}/libXvMC.so
%{_libdir}/libXvMCW.la
%{_libdir}/libXvMC.la
%{_libdir}/pkgconfig/xvmc.pc
%{_includedir}/X11/extensions/XvMClib.h
%dir %{_docdir}/libXvMC
%{_docdir}/libXvMC/XvMC_API.txt

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} >= %{version}-%{release}
Provides: libxvmc-static-devel = %{version}-%{release}
Provides: libxvmc1-static-devel = %{version}-%{release}
Obsoletes: %{mklibname xvmc 1 -s -d}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libXvMCW.a
%{_libdir}/libXvMC.a

#-----------------------------------------------------------

%prep
%setup -q -n libXvMC-%{version}

%build
export LIBS="-ldl"

%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libXvMC.so.1
%{_libdir}/libXvMC.so.1.0.0
%{_libdir}/libXvMCW.so.1
%{_libdir}/libXvMCW.so.1.0.0
