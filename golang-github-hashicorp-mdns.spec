# http://github.com/hashicorp/mdns
%global provider_prefix github.com/hashicorp/mdns
%global gobaseipath     %{provider_prefix}
%global commit          2b439d37011456df8ff83a70ffd1cd6046410113
%global commitdate      20150317

%gocraftmeta -i

Name:           %{goname}
Version:        0
Release:        0.12.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Simple mDNS client/server library in Golang 
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Patch0:         change-import-path-of-go.net.patch

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(golang.org/x/net/ipv4)
BuildRequires: golang(golang.org/x/net/ipv6)
BuildRequires: golang(github.com/miekg/dns)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{gobaseipath} prefix.

%prep
%gosetup
%patch0 -p1

%install
%goinstall

%check
%gochecks %{gobaseipath}

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.20150317git2b439d3
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git2b439d3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git2b439d3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git2b439d3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git2b439d3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git2b439d3
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git2b439d3
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git2b439d3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git2b439d3
- Update to spec-2.1
  related: #1250470

* Mon Aug 10 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git2b439d3
- Update dependencies on go.net
  related: #1250470

* Wed Aug 05 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.git2b439d3
- Update spec file to spec-2.0
  resolves: #1250470

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git2b439d3
- First package for Fedora
  resolves: #1212116

