%define		kdeplasmaver	5.11.0
%define		qtver		5.5.1
%define		kpname		discover
Summary:	discover
Name:		kp5-%{kpname}
Version:	5.11.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	5cb5de24ee185a7c07c70165b81cd9d2
URL:		http://www.kde.org/
BuildRequires:	Qt5Concurrent-devel >= %{qtver}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-karchive-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kitemviews-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-ktextwidgets-devel
BuildRequires:	kf5-kwallet-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-solid-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
discover

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang discover --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f discover.lang
%defattr(644,root,root,755)
%dir %{_libdir}/qt5/plugins/discover
%attr(755,root,root) %{_libdir}/qt5/plugins/discover/kns-backend.so
%dir %{_libdir}/qt5/qml/org/kde/discovernotifier
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/discovernotifier/libDiscoverNotifierDeclarativePlugin.so
%{_desktopdir}/org.kde.discover.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.discovernotifier.desktop
%{_datadir}/plasma/plasmoids/org.kde.discovernotifier
/etc/xdg/discover_ktexteditor_codesnippets_core.knsrc
%{_libdir}/qt5/qml/org/kde/discovernotifier/qmldir
%attr(755,root,root) %{_bindir}/plasma-discover
%{_libdir}/plasma-discover
%{_desktopdir}/org.kde.discover.urlhandler.desktop
%{_iconsdir}/hicolor/128x128/apps/plasmadiscover.png
%{_iconsdir}/hicolor/16x16/apps/plasmadiscover.png
%{_iconsdir}/hicolor/22x22/apps/plasmadiscover.png
%{_iconsdir}/hicolor/32x32/apps/plasmadiscover.png
%{_iconsdir}/hicolor/48x48/apps/plasmadiscover.png
%{_iconsdir}/hicolor/scalable/apps/plasmadiscover.svgz
%{_datadir}/knotifications5/discoverabstractnotifier.notifyrc
%dir %{_datadir}/kxmlgui5/plasmadiscover
%{_datadir}/kxmlgui5/plasmadiscover/plasmadiscoverui.rc
%{_datadir}/metainfo/org.kde.discover.appdata.xml
%{_datadir}/metainfo/org.kde.discovernotifier.appdata.xml
