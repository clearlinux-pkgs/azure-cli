#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-cli
Version  : 2.5.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/cb/e2/68dce3a5cd798faa54e105411902ab9db1f54ea5774c78b3d54e6a38df1d/azure-cli-2.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/cb/e2/68dce3a5cd798faa54e105411902ab9db1f54ea5774c78b3d54e6a38df1d/azure-cli-2.5.0.tar.gz
Summary  : Microsoft Azure Command-Line Tools
Group    : Development/Tools
License  : BSD-2-Clause MIT
Requires: azure-cli-bin = %{version}-%{release}
Requires: azure-cli-license = %{version}-%{release}
Requires: azure-cli-python = %{version}-%{release}
Requires: azure-cli-python3 = %{version}-%{release}
Requires: azure-nspkg
Requires: pip
Requires: requests
Requires: setuptools
Requires: wheel
BuildRequires : azure-nspkg
BuildRequires : buildreq-distutils3
BuildRequires : pip
BuildRequires : requests
BuildRequires : setuptools
BuildRequires : wheel

%description
A great cloud needs great tools; we're excited to introduce Azure CLI,
 our next generation multi-platform command line experience for Azure.

%package bin
Summary: bin components for the azure-cli package.
Group: Binaries
Requires: azure-cli-license = %{version}-%{release}

%description bin
bin components for the azure-cli package.


%package license
Summary: license components for the azure-cli package.
Group: Default

%description license
license components for the azure-cli package.


%package python
Summary: python components for the azure-cli package.
Group: Default
Requires: azure-cli-python3 = %{version}-%{release}

%description python
python components for the azure-cli package.


%package python3
Summary: python3 components for the azure-cli package.
Group: Default
Requires: python3-core
Provides: pypi(azure_cli)
Requires: pypi(antlr4_python3_runtime)
Requires: pypi(azure_batch)
Requires: pypi(azure_cli_command_modules_nspkg)
Requires: pypi(azure_cli_core)
Requires: pypi(azure_cli_nspkg)
Requires: pypi(azure_cli_telemetry)
Requires: pypi(azure_cosmos)
Requires: pypi(azure_datalake_store)
Requires: pypi(azure_functions_devops_build)
Requires: pypi(azure_graphrbac)
Requires: pypi(azure_keyvault)
Requires: pypi(azure_loganalytics)
Requires: pypi(azure_mgmt_advisor)
Requires: pypi(azure_mgmt_apimanagement)
Requires: pypi(azure_mgmt_appconfiguration)
Requires: pypi(azure_mgmt_applicationinsights)
Requires: pypi(azure_mgmt_authorization)
Requires: pypi(azure_mgmt_batch)
Requires: pypi(azure_mgmt_batchai)
Requires: pypi(azure_mgmt_billing)
Requires: pypi(azure_mgmt_botservice)
Requires: pypi(azure_mgmt_cdn)
Requires: pypi(azure_mgmt_cognitiveservices)
Requires: pypi(azure_mgmt_compute)
Requires: pypi(azure_mgmt_consumption)
Requires: pypi(azure_mgmt_containerinstance)
Requires: pypi(azure_mgmt_containerregistry)
Requires: pypi(azure_mgmt_containerservice)
Requires: pypi(azure_mgmt_cosmosdb)
Requires: pypi(azure_mgmt_datalake_analytics)
Requires: pypi(azure_mgmt_datalake_store)
Requires: pypi(azure_mgmt_datamigration)
Requires: pypi(azure_mgmt_deploymentmanager)
Requires: pypi(azure_mgmt_devtestlabs)
Requires: pypi(azure_mgmt_dns)
Requires: pypi(azure_mgmt_eventgrid)
Requires: pypi(azure_mgmt_eventhub)
Requires: pypi(azure_mgmt_hdinsight)
Requires: pypi(azure_mgmt_imagebuilder)
Requires: pypi(azure_mgmt_iotcentral)
Requires: pypi(azure_mgmt_iothub)
Requires: pypi(azure_mgmt_iothubprovisioningservices)
Requires: pypi(azure_mgmt_keyvault)
Requires: pypi(azure_mgmt_kusto)
Requires: pypi(azure_mgmt_loganalytics)
Requires: pypi(azure_mgmt_managedservices)
Requires: pypi(azure_mgmt_managementgroups)
Requires: pypi(azure_mgmt_maps)
Requires: pypi(azure_mgmt_marketplaceordering)
Requires: pypi(azure_mgmt_media)
Requires: pypi(azure_mgmt_monitor)
Requires: pypi(azure_mgmt_msi)
Requires: pypi(azure_mgmt_netapp)
Requires: pypi(azure_mgmt_network)
Requires: pypi(azure_mgmt_policyinsights)
Requires: pypi(azure_mgmt_privatedns)
Requires: pypi(azure_mgmt_rdbms)
Requires: pypi(azure_mgmt_recoveryservices)
Requires: pypi(azure_mgmt_recoveryservicesbackup)
Requires: pypi(azure_mgmt_redhatopenshift)
Requires: pypi(azure_mgmt_redis)
Requires: pypi(azure_mgmt_relay)
Requires: pypi(azure_mgmt_reservations)
Requires: pypi(azure_mgmt_resource)
Requires: pypi(azure_mgmt_search)
Requires: pypi(azure_mgmt_security)
Requires: pypi(azure_mgmt_servicebus)
Requires: pypi(azure_mgmt_servicefabric)
Requires: pypi(azure_mgmt_signalr)
Requires: pypi(azure_mgmt_sql)
Requires: pypi(azure_mgmt_sqlvirtualmachine)
Requires: pypi(azure_mgmt_storage)
Requires: pypi(azure_mgmt_trafficmanager)
Requires: pypi(azure_mgmt_web)
Requires: pypi(azure_multiapi_storage)
Requires: pypi(azure_storage_blob)
Requires: pypi(colorama)
Requires: pypi(cryptography)
Requires: pypi(fabric)
Requires: pypi(javaproperties)
Requires: pypi(jsmin)
Requires: pypi(jsondiff)
Requires: pypi(knack)
Requires: pypi(mock)
Requires: pypi(paramiko)
Requires: pypi(pyopenssl)
Requires: pypi(pytz)
Requires: pypi(requests)
Requires: pypi(scp)
Requires: pypi(six)
Requires: pypi(sshtunnel)
Requires: pypi(urllib3)
Requires: pypi(vsts_cd_manager)
Requires: pypi(websocket_client)
Requires: pypi(xmltodict)

%description python3
python3 components for the azure-cli package.


%prep
%setup -q -n azure-cli-azure-cli-2.5.0
cd %{_builddir}/azure-cli-azure-cli-2.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588614181
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
pushd src/azure-cli
python3 setup.py build  ||:

popd
## build_append content
extra_pkgs="azure-cli-command_modules-nspkg azure-cli-core azure-cli-nspkg azure-cli-telemetry azure-cli-testsdk"

for pkg in $extra_pkgs; do
pushd src/$pkg
python3 setup.py build
popd
done
## build_append end
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/azure-cli
cp %{_builddir}/azure-cli-azure-cli-2.5.0/LICENSE %{buildroot}/usr/share/package-licenses/azure-cli/54a77c8707aad5e56ac001d78c221c860ad5a7d0
cp %{_builddir}/azure-cli-azure-cli-2.5.0/src/azure-cli/LICENSE.txt %{buildroot}/usr/share/package-licenses/azure-cli/7d8a62cc5b0bc6fd21840d3804a5d62b9e6f1366
cp %{_builddir}/azure-cli-azure-cli-2.5.0/src/azure-cli/azure/cli/command_modules/appservice/fabric_license %{buildroot}/usr/share/package-licenses/azure-cli/34710b3b270a12abfe1210d0f2c022491365c095
pushd src/azure-cli
python3 -tt setup.py build  install --root=%{buildroot}
popd
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
extra_pkgs="azure-cli-command_modules-nspkg azure-cli-core azure-cli-nspkg azure-cli-telemetry azure-cli-testsdk"

for pkg in $extra_pkgs; do
pushd src/$pkg
python3 -tt setup.py build  install --root=%{buildroot}
popd
done

mkdir -p %{buildroot}/bin
printf "#!/usr/bin/env bash\nAZ_INSTALLER=RPM PYTHONPATH=/usr/bin/python -sm azure.cli \"\$@\"" > %{buildroot}/bin/az
chmod 755 %{buildroot}/bin/az
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/bin/az
/usr/bin/az
/usr/bin/az.bat
/usr/bin/az.completion.sh

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/azure-cli/34710b3b270a12abfe1210d0f2c022491365c095
/usr/share/package-licenses/azure-cli/54a77c8707aad5e56ac001d78c221c860ad5a7d0
/usr/share/package-licenses/azure-cli/7d8a62cc5b0bc6fd21840d3804a5d62b9e6f1366

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
