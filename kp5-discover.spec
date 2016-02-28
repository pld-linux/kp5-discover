%define		kdeplasmaver	5.5.4
%define		qtver		5.5.1
%define		kpname		discover
Summary:	discover
Name:		kp5-%{kpname}
Version:	5.5.4
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	277ad0f67e0b101d109e93a03902bf49
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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f discover.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/muon-discover
%attr(755,root,root) %{_bindir}/muon-updater
%attr(755,root,root) %{_libdir}/libDiscoverCommon.so
%attr(755,root,root) %{_libdir}/libDiscoverNotifiers.so
%attr(755,root,root) %{_libdir}/qt5/plugins/discover/kns-backend.so
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/discover/libdiscoverdeclarativeplugin.so
%{_libdir}/qt5/qml/org/kde/discover/qmldir
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/discovernotifier/libDiscoverNotifierDeclarativePlugin.so
%{_libdir}/qt5/qml/org/kde/discovernotifier/qmldir
%{_desktopdir}/muon-updater.desktop
%{_desktopdir}/org.kde.discover.desktop
%{_iconsdir}/hicolor/128x128/apps/muondiscover.png
%{_iconsdir}/hicolor/16x16/apps/muondiscover.png
%{_iconsdir}/hicolor/22x22/apps/muondiscover.png
%{_iconsdir}/hicolor/32x32/apps/muondiscover.png
%{_iconsdir}/hicolor/48x48/apps/muondiscover.png
%{_iconsdir}/hicolor/scalable/apps/muondiscover.svgz
%{_datadir}/knotifications5/muonabstractnotifier.notifyrc
%{_datadir}/kservices5/plasma-applet-org.kde.discovernotifier.desktop
%{_datadir}/kxmlgui5/muondiscover/muondiscoverui.rc
%{_datadir}/kxmlgui5/muonupdater/muonupdaterui.rc
%{_datadir}/libdiscover/backends/knscomics-backend.desktop
%{_datadir}/libdiscover/backends/knsplasmoids-backend.desktop
%{_datadir}/libdiscover/categories/knscomics-backend-categories.xml
%{_datadir}/libdiscover/categories/knsplasmoids-backend-categories.xml
%{_datadir}/muondiscover/featured.json
%{_datadir}/plasma/plasmoids/org.kde.discovernotifier/contents/ui/Full.qml
%{_datadir}/plasma/plasmoids/org.kde.discovernotifier/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.discovernotifier/metadata.desktop
