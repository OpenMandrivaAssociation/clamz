%define name clamz
%define version 0.4
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

