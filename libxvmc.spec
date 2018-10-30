%define major 1
%define libname %mklibname xvmc %{major}
%define libw %mklibname xvmcw %{major}
%define devname %mklibname xvmc -d

Summary:	The XvMC Library
Name:		libxvmc
Version:	1.0.10
Release:	2
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXvMC-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xext) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros) >= 1.0.1
BuildRequires:	pkgconfig(xproto) >= 1.0.0
BuildRequires:	pkgconfig(xv) >= 1.0.1

%description
The XvMC Library.

%package -n %{libname}
Summary:	The XvMC Library
Group:		Development/X11
Provides:	%{name} = %{version}-%{release}

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

%prep
%setup -qn libXvMC-%{version}

%build
export LIBS="-ldl"

%configure \
	--disable-static \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXvMC.so.%{major}*

%files -n %{libw}
%{_libdir}/libXvMCW.so.%{major}*

%files -n %{devname}
%{_libdir}/libXvMCW.so
%{_libdir}/libXvMC.so
%{_libdir}/pkgconfig/xvmc.pc
%{_includedir}/X11/extensions/XvMClib.h
%dir %{_docdir}/libXvMC
%{_docdir}/libXvMC/XvMC_API.txt

