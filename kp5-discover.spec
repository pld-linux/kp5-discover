#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.27.11
%define		qtver		5.15.2
%define		kpname		discover
Summary:	discover
Name:		kp5-%{kpname}
Version:	5.27.11
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	91c91a2c8efc546e8fc53f97c8aa5834
URL:		http://www.kde.org/
BuildRequires:	AppStream-qt-devel >= 0.15.3
BuildRequires:	Qt5Concurrent-devel >= %{qtver}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= %{qtver}
BuildRequires:	Qt5Quick-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5WebView-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	flatpak-devel
BuildRequires:	fwupd-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-karchive-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kidletime-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kitemmodels-devel
BuildRequires:	kf5-kitemviews-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-ktextwidgets-devel
BuildRequires:	kf5-kwallet-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-purpose-devel
BuildRequires:	kf5-solid-devel
BuildRequires:	libmarkdown-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Suggests:	flatpak
Suggests:	fwupd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
discover

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

# not supported by glibc yet
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang discover --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f discover.lang
%defattr(644,root,root,755)
%dir %{_libdir}/qt5/plugins/discover
%attr(755,root,root) %{_libdir}/qt5/plugins/discover/fwupd-backend.so
%{_desktopdir}/org.kde.discover.desktop
%attr(755,root,root) %{_bindir}/plasma-discover
%{_libdir}/plasma-discover
%{_desktopdir}/org.kde.discover.urlhandler.desktop
%{_iconsdir}/hicolor/128x128/apps/plasmadiscover.png
%{_iconsdir}/hicolor/16x16/apps/plasmadiscover.png
%{_iconsdir}/hicolor/22x22/apps/plasmadiscover.png
%{_iconsdir}/hicolor/32x32/apps/plasmadiscover.png
%{_iconsdir}/hicolor/48x48/apps/plasmadiscover.png
%{_iconsdir}/hicolor/scalable/apps/plasmadiscover.svg*
%dir %{_datadir}/kxmlgui5/plasmadiscover
%{_datadir}/kxmlgui5/plasmadiscover/plasmadiscoverui.rc
%{_datadir}/metainfo/org.kde.discover.appdata.xml
/etc/xdg/autostart/org.kde.discover.notifier.desktop
%attr(755,root,root) %{_libexecdir}/DiscoverNotifier
%{_desktopdir}/org.kde.discover.notifier.desktop
%{_datadir}/knotifications5/discoverabstractnotifier.notifyrc
%{_datadir}/qlogging-categories5/discover.categories
%attr(755,root,root) %{_bindir}/plasma-discover-update
%{_desktopdir}/org.kde.discover.snap.desktop
%dir %{_datadir}/kpackage/kcms/kcm_updates
%dir %{_datadir}/kpackage/kcms/kcm_updates/contents
%dir %{_datadir}/kpackage/kcms/kcm_updates/contents/ui
%{_datadir}/kpackage/kcms/kcm_updates/contents/ui/main.qml
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_updates.so
%{_desktopdir}/kcm_updates.desktop
%dir %{_libdir}/qt5/plugins/discover-notifier
%{_libdir}/qt5/plugins/discover-notifier/FlatpakNotifier.so
%{_libdir}/qt5/plugins/discover/flatpak-backend.so
%{_libdir}/qt5/plugins/discover/kns-backend.so
%{_desktopdir}/org.kde.discover-flatpak.desktop
%{_iconsdir}/hicolor/scalable/apps/flatpak-discover.svg
%dir %{_datadir}/libdiscover
%dir %{_datadir}/libdiscover/categories
%{_datadir}/libdiscover/categories/flatpak-backend-categories.xml
%{_datadir}/metainfo/org.kde.discover.flatpak.appdata.xml
