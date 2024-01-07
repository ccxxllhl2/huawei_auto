from ncclient import manager

ip = "192.168.56.100"
nc_port = 830
nc_user = "netconf"
nc_pass = "Huawei123@"

# 1. 开启连接
nc_proc = manager.connect(host=ip,
                          port=nc_port,
                          username=nc_user,
                          password=nc_pass,
                          hostkey_verify=False,
                          device_params={'name': 'huawei'})

def if_get_config():
    # 2. 编写配置或过滤器
    Filter = '''
    <filter type="subtree">
          <ifm xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
            <interfaces>
              <interface>
                 <ifName>GE1/0/1</ifName>
                 <isL2SwitchPort></isL2SwitchPort>
                 <ifAdminStatus></ifAdminStatus>
              </interface>
            </interfaces>
          </ifm>
        </filter>
    '''

    # 3. 编写操作
    result = str(nc_proc.get_config(source='running', filter=Filter))
    l2_port = result.split('<isL2SwitchPort>')[1].split('</isL2SwitchPort>')[0]
    admin_port = result.split('<ifAdminStatus>')[1].split('</ifAdminStatus>')[0]
    print(f"端口 GE1/0/1 当前L2状态是 {l2_port} ，管理状态是 {admin_port}")

def if_edit():
    Config = '''
    <config>
        <ethernet xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
            <ethernetIfs>
              <ethernetIf operation="merge">
                <ifName>GE1/0/1</ifName>
                <l2Enable>disable</l2Enable>
              </ethernetIf>
            </ethernetIfs>
        </ethernet>

       <ifm xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
         <interfaces>
           <interface operation="merge">
             <ifName>GE1/0/1</ifName>
             <ifAdminStatus>up</ifAdminStatus>
           </interface>
         </interfaces>
       </ifm>
     </config>
    '''
    nc_proc.edit_config(target='running', config=Config)

if_get_config()
if_edit()
if_get_config()
nc_proc.close_session()
