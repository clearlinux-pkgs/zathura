#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : zathura
Version  : 0.5.2
Release  : 28
URL      : https://github.com/pwmt/zathura/archive/0.5.2/zathura-0.5.2.tar.gz
Source0  : https://github.com/pwmt/zathura/archive/0.5.2/zathura-0.5.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Zlib
Requires: zathura-bin = %{version}-%{release}
Requires: zathura-data = %{version}-%{release}
Requires: zathura-filemap = %{version}-%{release}
Requires: zathura-license = %{version}-%{release}
Requires: zathura-locales = %{version}-%{release}
Requires: zathura-man = %{version}-%{release}
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
BuildRequires : pypi-sphinx
BuildRequires : sqlite-autoconf-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
Requires: zathura-filemap = %{version}-%{release}

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


%package filemap
Summary: filemap components for the zathura package.
Group: Default

%description filemap
filemap components for the zathura package.


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
%setup -q -n zathura-0.5.2
cd %{_builddir}/zathura-0.5.2
pushd ..
cp -a zathura-0.5.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1682405827
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dsynctex=disabled  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dsynctex=disabled  builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/zathura
cp %{_builddir}/zathura-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/zathura/840d80c2a1107d620abfb72ce18e40d5ca2d0cc1 || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang zathura
## install_append content
mkdir -p %{buildroot}/{,V3,V4}/usr/bin
echo -n -e \\x7f\\x45\\x4c\\x46\\xf0 > %{buildroot}/usr/bin/aa1-mixer-test-canary-0
echo -n -e \\x7f\\x45\\x4c\\x46\\xf1 > %{buildroot}/usr/bin/aa1-mixer-test-canary-1
echo -n -e \\x7f\\x45\\x4c\\x46\\xf2 > %{buildroot}/usr/bin/aa1-mixer-test-canary-2
echo -n -e \\x7f\\x45\\x4c\\x46\\xf3 > %{buildroot}/usr/bin/aa1-mixer-test-canary-3
echo -n -e \\x7f\\x45\\x4c\\x46\\xf4 > %{buildroot}/V3/usr/bin/aa1-mixer-test-canary-1
echo -n -e \\x7f\\x45\\x4c\\x46\\xf7 > %{buildroot}/V4/usr/bin/aa1-mixer-test-canary-3
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/aa1-mixer-test-canary-1
/V4/usr/bin/aa1-mixer-test-canary-3
/usr/bin/aa1-mixer-test-canary-0
/usr/bin/aa1-mixer-test-canary-1
/usr/bin/aa1-mixer-test-canary-2
/usr/bin/aa1-mixer-test-canary-3
/usr/bin/zathura
/usr/share/clear/optimized-elf/bin*

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

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-zathura

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zathura/840d80c2a1107d620abfb72ce18e40d5ca2d0cc1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/zathura.1
/usr/share/man/man5/zathurarc.5

%files locales -f zathura.lang
%defattr(-,root,root,-)

