%define name clamz
%define version 0.5
%define release %mkrel 1

Summary: Command-line downloader for the amazon.com MP3 music store
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://clamz.googlecode.com/files/%{name}-%{version}.tar.gz
License: GPLv3
Group: Networking/WWW
Url: http://code.google.com/p/clamz/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgcrypt-devel
BuildRequires: curl-devel
BuildRequires: expat-devel
BuildRequires: shared-mime-info
BuildRequires: desktop-file-utils


%description
Clamz is a little command-line program to download MP3 files from
Amazon.com's music store. It is intended to serve as a substitute for
Amazon's official MP3 Downloader, which is not free software (and
therefore is only available in binary form for a limited set of
platforms.) Clamz can be used to download either individual songs or
complete albums that you have purchased from Amazon.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std UPDATE_MIME_DATABASE=true UPDATE_DESKTOP_DATABASE=true
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%_bindir/%name
%_datadir/man/man1/%name.1*
%_datadir/applications/%name.desktop
%_datadir/mime/packages/%name.xml



%changelog
* Sun Oct 30 2011 Götz Waschk <waschk@mandriva.org> 0.5-1mdv2011.0
+ Revision: 707907
- update to new version 0.5

* Mon Jul 11 2011 Götz Waschk <waschk@mandriva.org> 0.4-2
+ Revision: 689500
- rebuild

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 0.4-1mdv2011.0
+ Revision: 550263
- new version

* Thu Apr 01 2010 Götz Waschk <waschk@mandriva.org> 0.3-1mdv2010.1
+ Revision: 530579
- new version
- use included desktop and mime database files

* Fri Dec 04 2009 Götz Waschk <waschk@mandriva.org> 0.2-3mdv2010.1
+ Revision: 473436
- don't show it in the menu

* Wed Nov 11 2009 Götz Waschk <waschk@mandriva.org> 0.2-2mdv2010.1
+ Revision: 465073
- add desktop entry and mime type

* Wed Nov 11 2009 Götz Waschk <waschk@mandriva.org> 0.2-1mdv2010.1
+ Revision: 464996
- import clamz

