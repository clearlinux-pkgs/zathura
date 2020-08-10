#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zathura
Version  : 0.4.6
Release  : 7
URL      : https://github.com/pwmt/zathura/archive/0.4.6/zathura-0.4.6.tar.gz
Source0  : https://github.com/pwmt/zathura/archive/0.4.6/zathura-0.4.6.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Zlib
Requires: zathura-bin = %{version}-%{release}
Requires: zathura-data = %{version}-%{release}
Requires: zathura-license = %{version}-%{release}
Requires: zathura-locales = %{version}-%{release}
Requires: zathura-man = %{version}-%{release}
BuildRequires : Sphinx
BuildRequires : appstream-glib
BuildRequires : bash-completion-dev
BuildRequires : buildreq-meson
BuildRequires : desktop-file-utils
BuildRequires : file-dev
BuildRequires : librsvg
BuildRequires : libseccomp-dev
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(fish)
BuildRequires : pkgconfig(girara-gtk3)
BuildRequires : pkgconfig(libseccomp)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(synctex)
BuildRequires : sqlite-autoconf-dev

%description
zathura - a document viewer
===========================
zathura is a highly customizable and functional document viewer based on the
girara user interface library and several document libraries.

%package bin
Summary: bin components for the zathura package.
Group: Binaries
Requires: zathura-data = %{version}-%{release}
Requires: zathura-license = %{version}-%{release}

%description bin
bin components for the zathura package.


%package data
Summary: data components for the zathura package.
Group: Data

%description data
data components for the zathura package.


%package dev
Summary: dev components for the zathura package.
Group: Development
Requires: zathura-bin = %{version}-%{release}
Requires: zathura-data = %{version}-%{release}
Provides: zathura-devel = %{version}-%{release}
Requires: zathura = %{version}-%{release}

%description dev
dev components for the zathura package.


%package license
Summary: license components for the zathura package.
Group: Default

%description license
license components for the zathura package.


%package locales
Summary: locales components for the zathura package.
Group: Default

%description locales
locales components for the zathura package.


%package man
Summary: man components for the zathura package.
Group: Default

%description man
man components for the zathura package.


%prep
%setup -q -n zathura-0.4.6
cd %{_builddir}/zathura-0.4.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597080691
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/zathura
cp %{_builddir}/zathura-0.4.6/LICENSE %{buildroot}/usr/share/package-licenses/zathura/840d80c2a1107d620abfb72ce18e40d5ca2d0cc1
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang zathura

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/zathura

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.pwmt.zathura.desktop
/usr/share/bash-completion/completions/zathura
/usr/share/dbus-1/interfaces/org.pwmt.zathura.xml
/usr/share/fish/vendor_completions.d/zathura.fish
/usr/share/icons/hicolor/128x128/apps/org.pwmt.zathura.png
/usr/share/icons/hicolor/16x16/apps/org.pwmt.zathura.png
/usr/share/icons/hicolor/256x256/apps/org.pwmt.zathura.png
/usr/share/icons/hicolor/32x32/apps/org.pwmt.zathura.png
/usr/share/icons/hicolor/64x64/apps/org.pwmt.zathura.png
/usr/share/icons/hicolor/scalable/apps/org.pwmt.zathura.svg
/usr/share/metainfo/org.pwmt.zathura.appdata.xml
/usr/share/zsh/site-functions/_zathura

%files dev
%defattr(-,root,root,-)
/usr/include/zathura/document.h
/usr/include/zathura/links.h
/usr/include/zathura/macros.h
/usr/include/zathura/page.h
/usr/include/zathura/plugin-api.h
/usr/include/zathura/types.h
/usr/include/zathura/zathura-version.h
/usr/lib64/pkgconfig/zathura.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zathura/840d80c2a1107d620abfb72ce18e40d5ca2d0cc1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/zathura.1
/usr/share/man/man5/zathurarc.5

%files locales -f zathura.lang
%defattr(-,root,root,-)

