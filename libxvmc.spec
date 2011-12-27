%define major 1
%define libname %mklibname xvmc %{major}
%define develname %mklibname xvmc -d

Name: libxvmc
Summary:  The XvMC Library
Version: 1.0.6
Release: 4
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXvMC-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxv-devel >= 1.0.1
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The XvMC Library

%package -n %{libname}
Summary:  The XvMC Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
The XvMC Library

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libname} = %{version}-%{release}
Provides: libxvmc-devel = %{version}-%{release}
Obsoletes: %{_lib}xvmc1-devel
Obsoletes: %{_lib}xvmc-static-devel
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libXvMC-%{version}

%build
export LIBS="-ldl"

%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libname}
%{_libdir}/libXvMC.so.%{major}*
%{_libdir}/libXvMCW.so.%{major}*

%files -n %{develname}
%{_libdir}/libXvMCW.so
%{_libdir}/libXvMC.so
%{_libdir}/pkgconfig/xvmc.pc
%{_includedir}/X11/extensions/XvMClib.h
%dir %{_docdir}/libXvMC
%{_docdir}/libXvMC/XvMC_API.txt

