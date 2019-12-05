#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-openid
Version  : 2.2.5
Release  : 5
URL      : https://files.pythonhosted.org/packages/7b/8a/e94d18c666073280b8c0614b7e38cfaf0b129989e42f4ca713942b862f0a/python-openid-2.2.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/7b/8a/e94d18c666073280b8c0614b7e38cfaf0b129989e42f4ca713942b862f0a/python-openid-2.2.5.tar.gz
Summary  : OpenID support for servers and consumers.
Group    : Development/Tools
License  : Apache-2.0
Requires: python-openid-license = %{version}-%{release}
Requires: python-openid-python = %{version}-%{release}
Requires: python-openid-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
the OpenID decentralized identity system in your application.  Want to enable
        single sign-on for your web site?  Use the openid.consumer package.  Want to
        run your own OpenID server? Check out openid.server.  Includes example code
        and support for a variety of storage back-ends.

%package license
Summary: license components for the python-openid package.
Group: Default

%description license
license components for the python-openid package.


%package python
Summary: python components for the python-openid package.
Group: Default
Requires: python-openid-python3 = %{version}-%{release}

%description python
python components for the python-openid package.


%package python3
Summary: python3 components for the python-openid package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-openid package.


%prep
%setup -q -n python-openid-2.2.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541606209
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-openid
cp LICENSE %{buildroot}/usr/share/package-licenses/python-openid/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-openid/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
