#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		ksnakeduel
Summary:	ksnakeduel
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	ae24f6c53af268c36e203dae6d9552fd
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kguiaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
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

%description -l pl.UTF-8
KSnakeDuel jest prostym klonem Trona. Możesz grać w KSnakeDuela
przeciwko komputerowi lub przyjacielowi. Celem gry jest przeżyć
dłużej niż przeciwnik. Aby tego dokonać, unikaj ścian, własnego ogona
jak i ogona oponenta.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
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
%{_datadir}/qlogging-categories5/ksnakeduel.categories
%{_datadir}/knsrcfiles/ksnakeduel.knsrc
