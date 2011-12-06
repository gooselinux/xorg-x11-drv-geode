%define tarball xf86-video-geode
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

Summary:   Xorg X11 AMD Geode video driver
Name:      xorg-x11-drv-geode
Version:   2.11.4.1
Release:   1%{?dist}
URL:       http://www.x.org/wiki/AMDGeodeDriver
Source0:   http://xorg.freedesktop.org/releases/individual/driver/xf86-video-geode-%{version}.tar.bz2
License:   MIT
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Provides:  xorg-x11-drv-amd = %{version}-%{release}
Obsoletes: xorg-x11-drv-amd <= 2.7.7.7

ExclusiveArch: %{ix86}

BuildRequires: pkgconfig
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: xorg-x11-server-sdk
BuildRequires: xorg-x11-proto-devel

Requires:  xorg-x11-server-Xorg >= 1.1.0

BuildRequires: autoconf automake

%description 
X.Org X11 AMD Geode video driver.

%prep
%setup -q -n %{tarball}-%{version}

%build
autoreconf -v --install
%configure --disable-static --libdir=%{_libdir} --mandir=%{_mandir} \
	     --enable-visibility
make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall DESTDIR=$RPM_BUILD_ROOT

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

# Compat symlink for legacy driver name so existing xorg.conf's do not break
ln -s geode_drv.so $RPM_BUILD_ROOT%{_libdir}/xorg/modules/drivers/amd_drv.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/amd_drv.so
%{driverdir}/geode_drv.so
%{driverdir}/ztv_drv.so

%changelog
* Thu Sep 10 2009 Dave Airlie <airlied@redhat.com> 2.11.4.1-1
- geode 2.11.4.1

* Wed Aug 05 2009 Dave Airlie <airlied@redhat.com> 2.11.3-1
- geode 2.11.3 
- add abi/api patches + autoreconf

* Tue Aug 04 2009 Adam Jackson <ajax@redhat.com> 2.11.2-4
- Fix for new DPMS headers

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.2-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 2.11.2-2.1
- ABI bump

* Tue Jun 23 2009 Dave Airlie <airlied@redhat.com> 2.11.2-2
- update for new server ABI

* Tue May 12 2009 Chris Ball <cjb@laptop.org> 2.11.2-1
- fix crasher bug due to EXA ABI change: RHBZ #500086

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Chris Ball <cjb@laptop.org> 2.11.1-1
- update to 2.11.1
- this build works on the OLPC XO with upstream/Rawhide kernels

* Mon Dec 22 2008 Dave Airlie <airlied@redhat.com> 2.11.0-2
- update for new server API

* Wed Dec 10 2008 Warren Togami <wtogami@redhat.com> - 2.11.0-1
- update to 2.11.0 adds xrandr-1.2 and fixes cursor issues

* Wed Aug 20 2008 Warren Togami <wtogami@redhat.com> - 2.10.1-1
- update to 2.10.1

* Fri Jun 13 2008 Dennis Gilmore <dennis@ausil.us> 2.10.0-1
- update to 2.10.0  drop upstreamed patches

* Tue May 20 2008 Dennis Gilmore <dennis@ausil.us> 2.9.0-2
- apply patches for olpc

* Thu May 08 2008 Dennis Gilmore <dennis@ausil.us> 2.9.0-1
- update to 2.9.0
- adds olpc support for everything but DPMS

* Thu Apr 17 2008 Warren Togami <wtogami@redhat.com> 2.8.0-3
- Use libddc instead of unreliable BIOS DDC queries.

* Wed Apr 02 2008 Warren Togami <wtogami@redhat.com> 2.8.0-2
- License: MIT

* Wed Apr 02 2008 Warren Togami <wtogami@redhat.com> 2.8.0-1
- 2.8.0 rename from amd to geode
  compat symlink to old name retains old xorg.conf compat

* Fri Mar 14 2008 Warren Togami <wtogami@redhat.com> 2.7.7.7-2
- proper versioned provides

* Fri Mar 14 2008 Warren Togami <wtogami@redhat.com> 2.7.7.7-1
- 2.7.7.7

* Mon Mar 10 2008 Dave Airlie <airlied@redhat.com> 0.0-26.20080310
- finally pciaccess build for AMD

* Mon Mar 10 2008 Dave Airlie <airlied@redhat.com> 0.0-25.20080310
- resnapshot for pciaccess goodness

* Mon Mar 10 2008 Dave Airlie <airlied@redhat.com> 0.0-24.20070625
- pciaccess fixups

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0-23.20070625
- Autorebuild for GCC 4.3

* Wed Jun 25 2007 Dan Williams <dcbw@redhat.com> 0.0-22.20070625
- Udpate to git snapshot
   - Fix downscaling on the LX
   - cairo 1.4.4 and Xorg 1.3 fixes

* Wed Jun 13 2007 Dan Williams <dcbw@redhat.com> 0.0-21.20070613
- Udpate to git snapshot

* Mon May 07 2007 Dan Williams <dcbw@redhat.com> 0.0-21.20070504
- Cleanups and fixes from -Wall

* Fri May 04 2007 Dan Williams <dcbw@redhat.com> 0.0-20.20070504
- Better OOM handling
- RandR fixes

* Thu May 03 2007 Dan Williams <dcbw@redhat.com> 0.0-19.20070503
- Fix QueryImageAttributes handler for GX
- Get correct prototype for memset/memcpy

* Thu May 03 2007 Dan Williams <dcbw@redhat.com> 0.0-18.20070503
- VGA port fixes
- Fixes for Xv color key mode

* Fri Apr 27 2007 Adam Jackson <ajax@redhat.com> 0.0-17.20070427
- Fix alpha blending.

* Tue Apr 24 2007 Adam Jackson <ajax@redhat.com> 0.0-16.20070424
- Misc LX fixes.

* Thu Apr 19 2007 Adam Jackson <ajax@redhat.com> 0.0-15.20070418
- Disable compression on LX for now, it's busted.

* Wed Apr 18 2007 Adam Jackson <ajax@redhat.com> 0.0-14.20070418
- Geode LX branch work

* Sat Feb  3 2007 Dan Williams <dcbw@redhat.com> 0.0-13.20070203.olpc1
- Fix segfault when accel is disabled

* Tue Jan 16 2007 Adam Jackson <ajax@redhat.com> 0.0-13.20070116.olpc1
- Fix EXA setup.

* Mon Jan 15 2007 Adam Jackson <ajax@redhat.com> 0.0-12.20070115.olpc1
- More Xv fixes, mode sync wonkiness, distcheck fix.

* Thu Jan 11 2007 Adam Jackson <ajax@redhat.com> 0.0-11.20070111.olpc1
- Xv fixes, RANDR fixes, minor crash fix.

* Thu Jan 04 2007 Adam Jackson <ajax@redhat.com> 0.0-10.20070104.olpc1
- Pull from dev.laptop.org: RANDR support, misc cleanup.

* Thu Nov 9 2006 Adam Jackson <ajackson@redhat.com> 0.0-9.20061109git.olpc1
- Today's update: DCON support, etc.

* Mon Oct 16 2006 Adam Jackson <ajackson@redhat.com> 0.0-8.20061016git.fc7
- Today's snapshot: More Xv love.
- Add check for (and abort on existance of) .git directory in the work dir.

* Thu Oct 12 2006 Adam Jackson <ajackson@redhat.com> 0.0-7.20061012git.fc6
- Today's snapshot: Xv fixes.

* Fri Oct 6 2006 Adam Jackson <ajackson@redhat.com> 0.0-6.20060821git.fc6
- Add visibility fixes, and build with -fvisibility=hidden for size.

* Mon Aug 21 2006 Adam Jackson <ajackson@redhat.com> 0.0-5.20060821git.fc6
- Today's snapshot: EXA fixes.

* Wed Aug 16 2006 Adam Jackson <ajackson@redhat.com> 0.0-4.20060816git.fc6
- Un-reset the Release: number.

* Wed Aug 16 2006 Adam Jackson <ajackson@redhat.com> 0.0-1.20060816git.fc6
- git update: more Xv fixes.

* Wed Aug  9 2006 Adam Jackson <ajackson@redhat.com> 0.0-3.20060809git.fc6
- Fix FC5 Requires too.

* Wed Aug  9 2006 Adam Jackson <ajackson@redhat.com> 0.0-2.20060809git.fc6
- FC5 build fixes, mostly BuildRequires.

* Wed Aug  9 2006 Adam Jackson <ajackson@redhat.com> 0.0-1.20060809git.fc6
- git update: olpc dcon support, Xv fixes.
- Attempted support for building against FC5.

* Fri Jul  7 2006 Adam Jackson <ajackson@redhat.com> 0.0-0.git20060706.fc6
- Initial spec (from -nsc) and git snapshot.
