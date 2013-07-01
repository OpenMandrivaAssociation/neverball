Name:		neverball
Summary:	Arcade game
Version: 1.5.4
Release: %mkrel 3
Url:		http://icculus.org/neverball/
Source0:	http://icculus.org/neverball/%{name}-%{version}.tar.bz2
Patch0:		neverball-1.5.2-fix-locale-dir.patch
Patch1:		neverball-1.5.4-fix-linking.patch
Group:		Games/Arcade
License:	GPLv2+
Epoch:		1
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	SDL_mixer-devel SDL_image-devel SDL_ttf-devel libpng-devel libjpeg-devel
BuildRequires:	GL-devel
BuildRequires:	libphysfs-devel
Obsoletes:	neverputt
Provides:	neverputt

%description
Tilt the floor to roll the ball through the obstacle course
before time runs out.
This package inclutes neverputt, a golf game based on neverball.
Hardware accellerated OpenGL support with multitexture
(OpenGL 1.2.1 or greater) is required.

%prep
%setup -q
%apply_patches

%build
%make CFLAGS="$RPM_OPT_FLAGS -ansi `sdl-config --cflags`" ENABLE_NLS=1 DATADIR=%_gamesdatadir/%name/data

%install
rm -rf $RPM_BUILD_ROOT

install -m 755 -D %name %buildroot%_gamesbindir/%name
install -m 755 neverputt %buildroot%_gamesbindir/

mkdir -p $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}
rm -fr data/map-*/*.map
cp -a data $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
install -m 644 dist/*.desktop $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p %buildroot%_mandir/man6
install -m 644 dist/*.6 %buildroot%_mandir/man6

for res in 16 24 32 48 64 128 256; do
    mkdir -p %buildroot%_datadir/icons/hicolor/${res}x${res}/apps
    install -m 644 dist/neverball_${res}.png %buildroot%_datadir/icons/hicolor/${res}x${res}/apps/neverball.png
    install -m 644 dist/neverputt_${res}.png %buildroot%_datadir/icons/hicolor/${res}x${res}/apps/neverputt.png
done

cp -r locale %buildroot%_datadir/

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%files -f %name.lang
%defattr(644,root,root,755)
%doc CHANGES README
%doc doc/*
%attr(755,root,root) %{_gamesbindir}/%{name}
%attr(755,root,root) %{_gamesbindir}/neverputt
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*
%{_datadir}/applications/%name.desktop
%{_datadir}/applications/neverputt.desktop
%_datadir/icons/hicolor/*/apps/never*png
%_mandir/man6/neverball.6*
%_mandir/man6/neverputt.6*


%changelog
* Wed Dec 07 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1:1.5.4-3mdv2012.0
+ Revision: 738526
- fix linking
- yearly rebuild

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.5.4-2mdv2011.0
+ Revision: 613037
- the mass rebuild of 2010.1 packages

* Sun Sep 20 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1:1.5.4-1mdv2010.0
+ Revision: 445299
- update to new version 1.5.4

* Wed Sep 09 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.5.3-1mdv2010.0
+ Revision: 435898
- update to new version 1.5.3

* Fri Aug 28 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1:1.5.2-2mdv2010.0
+ Revision: 421827
- add another patch to fix locale dir
- drop patch and set datadir in make command line (bug #53233)

* Mon Aug 17 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1:1.5.2-1mdv2010.0
+ Revision: 417145
- update build deps
- new version
- drop patch 0

* Sun Aug 16 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1:1.5.1-5mdv2010.0
+ Revision: 416887
- rebuild for new libjpeg

* Fri Jun 12 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1:1.5.1-4mdv2010.0
+ Revision: 385557
- really fix directories (bug #51591)

* Fri Jun 12 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1:1.5.1-3mdv2010.0
+ Revision: 385475
- fix locale location
- readd wrapper scripts to make it start from command line again

* Fri Jun 12 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1:1.5.1-2mdv2010.0
+ Revision: 385389
- fix data dir
- use upstream desktop entries, icons, man pages and docs
- enable translations

* Mon Jun 08 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1:1.5.1-1mdv2010.0
+ Revision: 383900
- update to new version 1.5.1

* Wed Feb 04 2009 Zombie Ryushu <ryushu@mandriva.org> 1:1.5.0-1mdv2009.1
+ Revision: 337241
- Add libjpeg to Build Requires
- Add libpng to Build Requires

  + Michael Scherer <misc@mandriva.org>
    - update to new release

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1:1.4.0-7mdv2009.0
+ Revision: 253859
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1:1.4.0-5mdv2008.1
+ Revision: 148290
- drop old menu
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Aug 28 2007 Thierry Vignaud <tv@mandriva.org> 1:1.4.0-5mdv2008.0
+ Revision: 73096
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Mon Sep 04 2006 Götz Waschk <waschk@mandriva.org> 1.4.0-5mdv2007.0
- fix installation

* Wed Jul 05 2006 Götz Waschk <waschk@mandriva.org> 1:1.4.0-4mdv2007.0
- fix buildrequires
- xdg menu

* Wed May 10 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1:1.4.0-3mdk
- Rebuild
- use mkrel

* Mon May 09 2005 Götz Waschk <waschk@mandriva.org> 1.4.0-2mdk
- fix build on x86_64

* Wed Sep 15 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.4.0-1mdk
- New release 1.4.0

* Mon Sep 06 2004 Götz Waschk <waschk@linux-mandrake.com> 1.3.7-2mdk
- don't accidently remove .sol files (thanks to Fabien Brachere)

* Thu Aug 12 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.3.7-1mdk
- New release 1.3.7

* Sun Jul 25 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.3.6-1mdk
- New release 1.3.6

* Thu Jul 22 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.3.5-1mdk
- New release 1.3.5

* Wed Jul 14 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.3.4-1mdk
- New release 1.3.4

* Tue Jul 13 2004 Götz Waschk <waschk@linux-mandrake.com> 1.3.3-1mdk
- drop GLU dependancy
- New release 1.3.3

* Mon Jul 12 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.3.2-1mdk
- New release 1.3.2

* Wed Jul 07 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.3.1-1mdk
- New release 1.3.1

* Mon Jun 28 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.3.0-1mdk
- New release 1.3.0

* Mon Jun 21 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.2.7-1mdk
- New release 1.2.7

* Fri May 07 2004 Götz Waschk <waschk@linux-mandrake.com> 1.2.5-1mdk
- add source URL
- fix doc file listing
- New release 1.2.5

* Wed Apr 14 2004 Olivier Blin <blino@mandrake.org> 1.2.1-1mdk
- install neverputt files
- Obsoletes/Provides neverputt (merged in neverball)
- new release

* Fri Feb 06 2004 Olivier Blin <blino@mandrake.org> 1.1.0-2mdk
- don't ship unneeded files (map "source" files)

* Thu Feb 05 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.1.0-1mdk
- 1.1.0
- fix buildrequires (lib64..)

* Sun Nov 09 2003 Olivier Blin <oliv.blin@laposte.net> 1.0.0-2mdk
- keep 0.25.11-2mdk fixes (stupid me ...)

* Sun Nov 09 2003 Olivier Blin <oliv.blin@laposte.net> 1.0.0-1mdk
- 1.0.0
- add url in Source0

* Wed Oct 29 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.25.11-2mdk
- compile with $RPM_OPT_FLAGS
- don't list datadir twice in %%files

* Mon Oct 27 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.25.11-1mdk
- 0.25.11
- updated url
- move to %%{_gamesbindir} and %%{_gamesdatadir}

* Thu Oct 16 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.25.10-1mdk
- 0.25.10

* Wed Oct 01 2003 Götz Waschk <waschk@linux-mandrake.com> 0.25.6-1mdk
- new version

* Mon Sep 22 2003 Götz Waschk <waschk@linux-mandrake.com> 0.25.4-1mdk
- new version

