Name:		nixnote
Version:	1.4
Release:	2
Group:		Networking/Other
Summary:	Evernote-clone. Use with Evernote to remember everything
License:	GPLv2
URL:		http://nevernote.sourceforge.net/
Source0:	%{name}-%{version}_i386.tar.gz
Source1:	%{name}-%{version}_amd64.tar.gz
Patch:		%{name}.desktop-ru.patch
Requires:   java-openjdk
Obsoletes:	nevernote

%description
Evernote-clone. Use with Evernote to remember everything

%prep
%ifarch %ix86
%setup -q -b 0 -n %{name}
%else
%setup -q -b 1 -n %{name}
%endif

%patch -p0

%install
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 usr/bin/%{name}.sh %{buildroot}%{_bindir}/%{name}

install -d -m 755 %{buildroot}%{_datadir}/applications
install -m 644 usr/share/applications/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -a usr/share/%{name}/* %{buildroot}%{_datadir}/%{name}

#install -d -m 755 %{buildroot}%{_docdir}/%{name}
#install -m 644 usr/share/doc/%{name}/* %{buildroot}%{_docdir}/%{name}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
#%{_docdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}

%changelog
* Mon Nov 28 2011 Sergey Zhemoitel <serg@mandriva.org> 1.1-1mdv2012.0
+ Revision: 735076
- new release 1.1

* Sun Sep 11 2011 Sergey Zhemoitel <serg@mandriva.org> 1.0-1
+ Revision: 699387
- imported package nixnote

