%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		ksnakeduel
Summary:	ksnakeduel
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	3af0a6ef1bb71a256a335cec29213625
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.30.0
BuildRequires:	kf5-kcompletion-devel >= 5.30.0
BuildRequires:	kf5-kconfig-devel >= 5.30.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.30.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.30.0
BuildRequires:	kf5-kcrash-devel >= 5.30.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.30.0
BuildRequires:	kf5-kguiaddons-devel >= 5.30.0
BuildRequires:	kf5-ki18n-devel >= 5.30.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.30.0
BuildRequires:	kf5-kxmlgui-devel >= 5.30.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSnakeDuel is a simple Tron-Clone You can play KSnakeDuel against the
computer or a friend. The aim of the game is to live longer than your
opponent. To do that, avoid running into a wall, your own tail and
that of your opponent.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/ksnakeduel.categories
/etc/xdg/ksnakeduel.knsrc
%attr(755,root,root) %{_bindir}/ksnakeduel
%{_desktopdir}/org.kde.ksnakeduel.desktop
%{_datadir}/config.kcfg/ksnakeduel.kcfg
%{_iconsdir}/hicolor/128x128/apps/ksnakeduel.png
%{_iconsdir}/hicolor/16x16/apps/ksnakeduel.png
%{_iconsdir}/hicolor/22x22/apps/ksnakeduel.png
%{_iconsdir}/hicolor/256x256/apps/ksnakeduel.png
%{_iconsdir}/hicolor/32x32/apps/ksnakeduel.png
%{_iconsdir}/hicolor/48x48/apps/ksnakeduel.png
%{_iconsdir}/hicolor/64x64/apps/ksnakeduel.png
%{_datadir}/ksnakeduel
%{_datadir}/metainfo/org.kde.ksnakeduel.appdata.xml
