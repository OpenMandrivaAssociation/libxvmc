# libxvmc is used by mesa, mesa is used by wine and steam
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define major 1
%define libname %mklibname xvmc %{major}
%define libw %mklibname xvmcw %{major}
%define devname %mklibname xvmc -d
%define lib32name libxvmc%{major}
%define lib32w libxvmcw%{major}
%define dev32name libxvmc-devel

Summary:	The XvMC Library
Name:		libxvmc
Version:	1.0.13
Release:	2
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXvMC-%{version}.tar.xz

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xext) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros) >= 1.0.1
BuildRequires:	pkgconfig(xproto) >= 1.0.0
BuildRequires:	pkgconfig(xv) >= 1.0.1
%if %{with compat32}
BuildRequires:	devel(libX11)
BuildRequires:	devel(libXext)
BuildRequires:	devel(libXv)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmcp)
%endif

%description
The XvMC Library.

%package -n %{libname}
Summary:	The XvMC Library
Group:		Development/X11

%description -n %{libname}
The XvMC Library.

%package -n %{libw}
Summary:	The XvMCW Library
Group:		Development/X11
Conflicts:	%{_lib}xvmc1 < 1.0.7-7

%description -n %{libw}
The XvMCW Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libw} = %{version}-%{release}
Provides:	libxvmc-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%if %{with compat32}
%package -n %{lib32name}
Summary:	The XvMC Library (32-bit)
Group:		Development/X11
Provides:	%{name} = %{version}-%{release}

%description -n %{lib32name}
The XvMC Library.

%package -n %{lib32w}
Summary:	The XvMCW Library (32-bit)
Group:		Development/X11

%description -n %{lib32w}
The XvMCW Library.

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}
Requires:	%{lib32w} = %{version}-%{release}

%description -n %{dev32name}
Development files for %{name}.
%endif

%prep
%autosetup -n libXvMC-%{version} -p1
export CONFIGURE_TOP="$(pwd)"
export LIBS="-ldl"

%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif

mkdir build
cd build
%configure


%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libXvMC.so.%{major}*

%files -n %{libw}
%{_libdir}/libXvMCW.so.%{major}*

%files -n %{devname}
%{_libdir}/libXvMCW.so
%{_libdir}/libXvMC.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/X11/extensions/*.h
%dir %{_docdir}/libXvMC
%{_docdir}/libXvMC/XvMC_API.txt

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libXvMC.so.%{major}*

%files -n %{lib32w}
%{_prefix}/lib/libXvMCW.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libXvMCW.so
%{_prefix}/lib/libXvMC.so
%{_prefix}/lib/pkgconfig/*.pc
%endif
