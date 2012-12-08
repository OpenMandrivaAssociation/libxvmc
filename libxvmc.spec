%define major 1
%define libname %mklibname xvmc %{major}
%define develname %mklibname xvmc -d

Name: libxvmc
Summary:  The XvMC Library
Version: 1.0.7
Release: 5
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
Obsoletes: %{_lib}xvmc1-devel < 1.0.7
Obsoletes: %{_lib}xvmc-static-devel < 1.0.7
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

%changelog
* Fri Jul 20 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.7-5
+ Revision: 810381
- update to new version 1.0.7

* Thu Mar 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0.6-5
+ Revision: 783387
- Remove pre scriptlet to correct rpm upgrade moving from /usr/X11R6.

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.0.6-4
+ Revision: 745790
- rebuild
- disabled static build
- removed .la files
- cleaned up spec
- employed major macro

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.6-3
+ Revision: 662432
- mass rebuild

* Sun Feb 20 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.0.6-2
+ Revision: 638841
- dropped major from devel and static pkgs
- added proper provides and obsoletes

* Mon Aug 16 2010 Thierry Vignaud <tv@mandriva.org> 1.0.6-1mdv2011.0
+ Revision: 570275
- new release

* Tue Nov 10 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.5-2mdv2010.1
+ Revision: 464049
- Ship docs too

  + Thierry Vignaud <tv@mandriva.org>
    - fix build
    - new release

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.4-5mdv2010.0
+ Revision: 425958
- rebuild

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-4mdv2009.0
+ Revision: 229746
- fix build (-ldl)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Wed Jan 16 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.4-2mdv2008.1
+ Revision: 153700
- Update BuildRequires and rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Feb 15 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0.4-1mdv2007.0
+ Revision: 121452
- new release

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - rebuild to fix cooker uploading
    - X11R7.1
    - increment release
    - fixed more dependencies
    - Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

