Name:           xsifstat
Version:        1.0.1
Release:        1%{?dist}
Summary:        Tool for visualising XenServer VIF metrics
License:        LGPL+linking exception
Group:          Development/Other
URL:            https://github.com/xenserver/xsifstat/

Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xsifstat/archive?at=v1.0.1&format=tar.gz&prefix=xsifstat-1.0.1#/xsifstat-1.0.1.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xsifstat/archive?at=v1.0.1&format=tar.gz&prefix=xsifstat-1.0.1#/xsifstat-1.0.1.tar.gz) = 317d45f45b015ce911268facdc3eda397c93e2a4

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
Requires:       python

%description
The xsifstat is a tool to expose metrics of the XenServer network subsystem on
a per-VIF basis.

%prep
%autosetup -p1

%build
mkdir -p %{buildroot}
DESTDIR=%{buildroot} %{__make}

%install
rm -rf %{buildroot}
DESTDIR=%{buildroot}/opt/xensource/debug %{__make} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/opt/xensource/debug/xsifstat

%changelog
* Thu Dec 15 2016 Rob Hoes <rob.hoes@citrix.com> - 1.0.1-1
- git: Add metadata to the result of `git archive`

* Tue Apr 26 2016 Si Beaumont <simon.beaumont@citrix.com> - 1.0.0-1
- Update to 1.0.0

* Fri Jul 11 2014 John Else <john.else@citrix.com> - 0.2.0-1
- Initial package for planex
