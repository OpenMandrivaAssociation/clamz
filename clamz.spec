Summary:	Command-line downloader for the amazon.com MP3 music store
Name:		clamz
Version:	0.5
Release:	7
License:	GPLv3
Group:		Networking/WWW
Url:		http://code.google.com/p/clamz/
Source0:	http://clamz.googlecode.com/files/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: shared-mime-info
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libgcrypt)

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
%makeinstall_std UPDATE_MIME_DATABASE=true UPDATE_DESKTOP_DATABASE=true

%files
%doc README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/%{name}.1*

