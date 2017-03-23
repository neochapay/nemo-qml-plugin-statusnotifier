%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}

Name:       nemo-qml-plugin-statusnotifier
Summary:    Declarative plugin for StatusNotifier
Version:    1.0.0
Release:    1
Group:      System/Libraries
License:    LGPLv2.1+
URL:        https://github.com/coderus/nemo-qml-plugin-statusnotifier
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5DBus)

%description
Declarative plugin for StatusNotifier. Contains both Host and Item

%prep
%setup -q -n %{name}-%{version}

%build

%qtc_qmake5

%qtc_make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%dir %{_libdir}/qt5/qml/org/nemomobile/statusnotifier
%{_libdir}/qt5/qml/org/nemomobile/statusnotifier/libstatusnotifier.so
%{_libdir}/qt5/qml/org/nemomobile/statusnotifier/qmldir
%{_libdir}/qt5/qml/org/nemomobile/statusnotifier/plugins.qmltypes
