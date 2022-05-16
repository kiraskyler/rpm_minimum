Name:           helloworld
Version:        0.0.0
Release:        1%{?dist}
Summary:        simple app help learn rpm build

License:        GPL
URL:            https://none
Source:         ../SOURCE/helloworld-0.0.0.tar.gz

# 构建依赖
BuildRequires:  gcc, make

# 运行时依赖
# Requires:

%description
description simple app help for learn rpm build

%prep                           # 安装前
%setup -q                       # 先解压

%build                          # 编译方法
make

%install                        # 安装方法
mkdir -p $RPM_BUILD_ROOT/%{_bindir}                 # 先创建一个文件夹
make DESTDIR=$RPM_BUILD_ROOT/%{_bindir} install     # install通过make传入安装文件夹安装

# 文件，安装到系统的有哪些文件
# 文件权限
# 二进制文件
%files 
%defattr(-,root,root)
%{_bindir}/helloworld

%doc

%changelog
