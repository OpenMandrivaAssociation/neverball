Name:		neverball
Summary:	NeverBall arcade game
Version: 1.5.4
Release: %mkrel 1
Url:		http://icculus.org/neverball/
Source0:	http://icculus.org/neverball/%{name}-%{version}.tar.bz2
Patch:		neverball-1.5.2-fix-locale-dir.patch
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
%patch -p1

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
