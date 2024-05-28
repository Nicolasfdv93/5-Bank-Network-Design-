Project 5 - Bank Network Design & implementation - Devs Config

## ACCESS LAYER ##

## ALL SWITCHES ##

EEnable password cisco
No ip domain lookup
Line console 0
Password cisco
Login
Exit
Service password-encryption
Ip domain-name cisco.net
Username admin password cisco
Crypto key generate rsa
1024
Line vty 0 15
Login local
Transport input ssh
Ip ssh version 2
Exit

vlan 1000
name NATIVE

int ran gi0/1-2
switchport mode trunk
switchport trunk native vlan 1000
exit

## FLOOR-1-MGMT-SW ##

en
Conf t
Hostname F1-MGMT-SW
Banner motd #FLOOR-1-MGMT-SW#
vlan 10
name MGMT

int ran fa0/1-24
switchport mode access
switchport access vlan 10
switchport port-security maximum 2
switchport port-security mac-address sticky
switchport port-security violation shutdown
do wr

## FLOOR-1-RSCH-SW ##

en
Conf t
Hostname F1-RSCH-SW
Banner motd #FLOOR-1-RSCH-SW#

vlan 20
name RESEARCH

int ran fa0/1-24
switchport mode access
switchport access vlan 20
switchport port-security maximum 2
switchport port-security mac-address sticky
switchport port-security violation shutdown
do wr

## FLOOR-1-HR-SW ##

en
Conf t
Hostname F1-HR-SW
Banner motd #FLOOR-1-HR-SW#

vlan 30
name HR

int ran fa0/1-24
switchport mode access
switchport access vlan 30
switchport port-security maximum 2
switchport port-security mac-address sticky
switchport port-security violation shutdown
do wr


## FLOOR-2-MKT-SW ##

en
Conf t
Hostname F2-MKT-SW
Banner motd #FLOOR-1-MARKETING-SW#

vlan 40
name MKT

int ran fa0/1-24
switchport mode access
switchport access vlan 40
switchport port-security maximum 2
switchport port-security mac-address sticky
switchport port-security violation shutdown
do wr

## FLOOR-2-ACC-SW ##

en
Conf t
Hostname F2-ACC-SW
Banner motd #FLOOR-2-ACCOUNTING-SW#

vlan 50
name ACC

int ran fa0/1-24
switchport mode access
switchport access vlan 50
switchport port-security maximum 2
switchport port-security mac-address sticky
switchport port-security violation shutdown
do wr

## FLOOR-2-FINANCE-SW ##

en
Conf t
Hostname F2-FINANCE-SW
Banner motd #FLOOR-2-FINANCE-SW#

vlan 60
name FINANCE

int ran fa0/1-24
switchport mode access
switchport access vlan 60
switchport port-security maximum 2
switchport port-security mac-address sticky
switchport port-security violation shutdown
do wr

## FLOOR-3-LOG-SW ##

en
Conf t
Hostname F3-LOG-SW
Banner motd #FLOOR-3-LOGISTIC-SW#

vlan 70
name LOG&STORE

int ran fa0/1-24
switchport mode access
switchport access vlan 70
switchport port-security maximum 2
switchport port-security mac-address sticky
switchport port-security violation shutdown
do wr

## FLOOR-3-CUST-SW ##

en
Conf t
Hostname F3-CUST-SW
Banner motd #FLOOR-3-CUSTOMER-CARE-SW#

vlan 80
name CUST-CARE

int ran fa0/1-24
switchport mode access
switchport access vlan 80
switchport port-security maximum 2
switchport port-security mac-address sticky
switchport port-security violation shutdown
do wr

## FLOOR-3-GST-SW ##

en
Conf t
Hostname F3-GST-SW
Banner motd #FLOOR-3-GUEST-SW#

vlan 90
name GUEST

int ran fa0/1-24
switchport mode access
switchport access vlan 90
switchport port-security maximum 2
switchport port-security mac-address sticky
switchport port-security violation shutdown
do wr

## FLOOR-4-ADMIN-SW ##

en
Conf t
Hostname F4-ADMIN-SW
Banner motd #FLOOR-4-ADMIN-SW#

vlan 100
name ADMIN

int ran fa0/1-24
switchport mode access
switchport access vlan 100
switchport port-security maximum 2
switchport port-security mac-address sticky
switchport port-security violation shutdown
do wr

## FLOOR-4-ICT-SW ##

en
Conf t
Hostname F4-ICT-SW
Banner motd #FLOOR-4-ICT-SW#

vlan 110
name ICT

int ran fa0/1-24
switchport mode access
switchport access vlan 110
switchport port-security maximum 2
switchport port-security mac-address sticky
switchport port-security violation shutdown
do wr

## FLOOR-4-SVR-SW ##

en
Conf t
Hostname F4-SVR-SW
Banner motd #FLOOR-4-SERVERS-SW#

vlan 120
name SERVERS

int ran fa0/1-24
switchport mode access
switchport access vlan 120
switchport port-security maximum 2
switchport port-security mac-address sticky
switchport port-security violation shutdown
do wr

### DISTRIBUTION LAYER CONFIGURATION ###

## ALL L3-SW ##

En
Conf t
Line console 0
Pass cisco
Login
Exit
No ip domain-lookup
Enable pass cisco
Service password-encryption
Ip domain-name cisco.net
Username cisco password cisco
Crypto key generate rsa
1024
Line vty 0 15
Login local
Transport input ssh
Ip ssh version 2
Exit

//L3 int
int ran g1/0/3-8
switchport mode trunk
switchport trunk native vlan 1000
exit

//L2 int
int ran g1/0/1-2
no switchport
exit

## L3-SW-FLOOR-1 ##

En
Conf t
Hostname L3-SW-FLOOR-1
Banner motd #L3-SW-FLOOR-1#

int g1/0/1
ip address 10.10.10.1 255.255.255.252
exit

int g1/0/2
ip address 10.10.10.9 255.255.255.252
exit

vlan 10
name MANAGEMENT
vlan 20
name RESEARCH
vlan 30
name HR
vlan 40
name MARKETING
vlan 50
name ACCOUNTING
vlan 60
name FINANCE
vlan 1000
name NATIVE
exit

int vlan 10
no shut
ip address 192.168.10.1 255.255.255.192
ip helper-address 192.168.12.196
exit
int vlan 20
no shut
ip address 192.168.10.65 255.255.255.192
ip helper-address 192.168.12.196
exit
int vlan 30
no shut
ip address 192.168.10.129 255.255.255.192
ip helper-address 192.168.12.196
exit
int vlan 40
no shut
ip address 192.168.10.193 255.255.255.192
ip helper-address 192.168.12.196
exit
int vlan 50
no shut
ip address 192.168.11.1 255.255.255.192
ip helper-address 192.168.12.196
exit
int vlan 60
no shut
ip address 192.168.11.65 255.255.255.192
ip helper-address 192.168.12.196
exit

//OSPF
Ip routing
router ospf 10
Auto-cost reference-bandwidth 100000
network 10.10.10.0 0.0.0.3 area 0
network 10.10.10.8 0.0.0.3 area 0
network 192.168.10.0 0.0.0.63 area 0
network 192.168.10.64 0.0.0.63 area 0
network 192.168.10.128 0.0.0.63 area 0
network 192.168.10.192 0.0.0.63 area 0
network 192.168.11.0 0.0.0.63 area 0
network 192.168.11.64 0.0.0.63 area 0
exit
do wr

## L3-SW-FLOOR-2 ##

En
Conf t
Hostname L3-SW-FLOOR-2
Banner motd #L3-SW-FLOOR-2#

int g1/0/1
ip address 10.10.10.5 255.255.255.252
exit

int g1/0/2
ip address 10.10.10.13 255.255.255.252
exit

vlan 10
name MANAGEMENT
vlan 20
name RESEARCH
vlan 30
name HR
vlan 40
name MARKETING
vlan 50
name ACCOUNTING
vlan 60
name FINANCE
vlan 1000
name NATIVE
exit

int vlan 10
no shut
ip address 192.168.10.1 255.255.255.192
ip helper-address 192.168.12.196
exit
int vlan 20
no shut
ip address 192.168.10.65 255.255.255.192
ip helper-address 192.168.12.196
exit
int vlan 30
no shut
ip address 192.168.10.129 255.255.255.192
ip helper-address 192.168.12.196
exit
int vlan 40
no shut
ip address 192.168.10.193 255.255.255.192
ip helper-address 192.168.12.196
exit
int vlan 50
no shut
ip address 192.168.11.1 255.255.255.192
ip helper-address 192.168.12.196
exit
int vlan 60
no shut
ip address 192.168.11.65 255.255.255.192
ip helper-address 192.168.12.196
exit

//OSPF
Ip routing
router ospf 10
Auto-cost reference-bandwidth 100000
network 10.10.10.4 0.0.0.3 area 0
network 10.10.10.12 0.0.0.3 area 0
network 192.168.10.0 0.0.0.63 area 0
network 192.168.10.64 0.0.0.63 area 0
network 192.168.10.128 0.0.0.63 area 0
network 192.168.10.192 0.0.0.63 area 0
network 192.168.11.0 0.0.0.63 area 0
network 192.168.11.64 0.0.0.63 area 0
exit
do wr

## L3-SW-FLOOR-3 ##

En
Conf t
Hostname L3-SW-FLOOR-3
Banner motd #L3-SW-FLOOR-3#

int g1/0/1
ip address 10.10.10.41 255.255.255.252
exit
int g1/0/2
ip address 10.10.10.45 255.255.255.252
exit

vlan 70
name LOG&STORE
vlan 80
name CUST-CARE
vlan 90
name GUEST
vlan 100
name ADMIN
vlan 110
name ICT
vlan 120
name SERVERS
vlan 1000
name NATIVE
exit

int vlan 70
no shut
ip address 192.168.11.129 255.255.255.192
ip helper-address 192.168.12.196
exit
int vlan 80
no shut
ip address 192.168.11.193 255.255.255.192
ip helper-address 192.168.12.196
exit
int vlan 90
no shut
ip address 192.168.12.1 255.255.255.192
ip helper-address 192.168.12.196
exit
int vlan 100
no shut
ip address 192.168.12.65 255.255.255.192
ip helper-address 192.168.12.196
exit
int vlan 110
no shut
ip address 192.168.12.129 255.255.255.192
ip helper-address 192.168.12.196
exit
int vlan 120
no shut
ip address 192.168.12.193 255.255.255.192
ip helper-address 192.168.12.196
exit

//OSPF
Ip routing
router ospf 10
Auto-cost reference-bandwidth 100000
network 10.10.10.40 0.0.0.3 area 0
network 10.10.10.44 0.0.0.3 area 0
network 192.168.11.128 0.0.0.63 area 0
network 192.168.11.192 0.0.0.63 area 0
network 192.168.12.0 0.0.0.63 area 0
network 192.168.12.64 0.0.0.63 area 0
network 192.168.12.128 0.0.0.63 area 0
network 192.168.12.192 0.0.0.63 area 0
exit

do wr

## L3-SW-FLOOR-4 ##

En
Conf t
Hostname L3-SW-FLOOR-4
Banner motd #L3-SW-FLOOR-4#

int g1/0/1
ip address 10.10.10.53 255.255.255.252
exit
int g1/0/2
ip address 10.10.10.49 255.255.255.252
exit

vlan 70
name LOG&STORE
vlan 80
name CUST-CARE
vlan 90
name GUEST
vlan 100
name ADMIN
vlan 110
name ICT
vlan 120
name SERVERS
vlan 1000
name NATIVE
exit

int vlan 70
no shut
ip address 192.168.11.129 255.255.255.192
ip helper-address 192.168.12.196
exit
int vlan 80
no shut
ip address 192.168.11.193 255.255.255.192
ip helper-address 192.168.12.196
exit
int vlan 90
no shut
ip address 192.168.12.1 255.255.255.192
ip helper-address 192.168.12.196
exit
int vlan 100
no shut
ip address 192.168.12.65 255.255.255.192
ip helper-address 192.168.12.196
exit
int vlan 110
no shut
ip address 192.168.12.129 255.255.255.192
ip helper-address 192.168.12.196
exit
int vlan 120
no shut
ip address 192.168.12.193 255.255.255.192
ip dhcp helper-address 192.168.12.196
exit

//OSPF
Ip routing
router ospf 10
Auto-cost reference-bandwidth 100000
network 10.10.10.48 0.0.0.3 area 0
network 10.10.10.52 0.0.0.3 area 0
network 192.168.11.128 0.0.0.63 area 0
network 192.168.11.192 0.0.0.63 area 0
network 192.168.12.0 0.0.0.63 area 0
network 192.168.12.64 0.0.0.63 area 0
network 192.168.12.128 0.0.0.63 area 0
network 192.168.12.192 0.0.0.63 area 0
exit
do wr

### CORE LAYER CONFIGURATION ###

## ALL ROUTERS ##

En
Conf t
Line console 0
Pass cisco
Login
Exit
No ip domain-lookup
Enable pass cisco
Service password-encryption
Ip domain-name cisco.net
Username cisco password cisco
Crypto key generate rsa
1024
Line vty 0 15
Login local
Transport input ssh
Ip ssh version 2
Do wr

## R-FLOOR-1 ##

En
Conf t
Hostname R-FLOOR-1
Banner motd #ROUTER-FLOOR-1#

int g0/0
no shut
ip address 10.10.10.29 255.255.255.252
exit
int g0/1
no shut
ip address 10.10.10.2 255.255.255.252
exit
int g0/2
no shut
ip address 10.10.10.6 255.255.255.252
exit

int se0/0/0
no shut
clock rate 64000
ip address 10.10.10.33 255.255.255.252
exit
int se0/0/1 
no shut
clock rate 64000
ip address 10.10.10.17 255.255.255.252
exit

//OSPF
router ospf 10
Auto-cost reference-bandwidth 100000
network 10.10.10.0 0.0.0.3 area 0
network 10.10.10.4 0.0.0.3 area 0
network 10.10.10.16 0.0.0.3 area 0
network 10.10.10.28 0.0.0.3 area 0
network 10.10.10.32 0.0.0.3 area 0
exit
do wr

## R-FLOOR-2 ##

En
Conf t
Hostname R-FLOOR-2
Banner motd #ROUTER-FLOOR-2#

int g0/0
no shut
ip address 10.10.10.21 255.255.255.252
exit
int g0/1
no shut
ip address 10.10.10.10 255.255.255.252
exit
int g0/2
no shut
ip address 10.10.10.14 255.255.255.252
exit

int se0/0/0
no shut
ip address 10.10.10.18 255.255.255.252
exit
int se0/0/1 
no shut
clock rate 64000
ip address 10.10.10.25 255.255.255.252
exit

//OSPF
router ospf 10
Auto-cost reference-bandwidth 100000
network 10.10.10.8 0.0.0.3 area 0
network 10.10.10.12 0.0.0.3 area 0
network 10.10.10.16 0.0.0.3 area 0
network 10.10.10.20 0.0.0.3 area 0
network 10.10.10.24 0.0.0.3 area 0
exit
do wr

## R-FLOOR-3 ##

En
Conf t
Hostname R-FLOOR-3
Banner motd #ROUTER-FLOOR-3#

int g0/0
no shut
ip address 10.10.10.22 255.255.255.252
exit
int g0/1
no shut
ip address 10.10.10.42 255.255.255.252
exit
int g0/2
no shut
ip address 10.10.10.50 255.255.255.252
exit

int se0/0/0
no shut
ip address 10.10.10.34 255.255.255.252
exit
int se0/0/1 
no shut
clock rate 64000
ip address 10.10.10.37 255.255.255.252
exit

//OSPF
router ospf 10
Auto-cost reference-bandwidth 100000
network 10.10.10.20 0.0.0.3 area 0
network 10.10.10.32 0.0.0.3 area 0
network 10.10.10.36 0.0.0.3 area 0
network 10.10.10.40 0.0.0.3 area 0
network 10.10.10.48 0.0.0.3 area 0
exit 
do wr

## R-FLOOR-4 ##

En
Conf t
Hostname R-FLOOR-4
Banner motd #ROUTER-FLOOR-4#

int g0/0
no shut
ip address 10.10.10.30 255.255.255.252
exit
int g0/1
no shut
ip address 10.10.10.46 255.255.255.252
exit
int g0/2
no shut
ip address 10.10.10.54 255.255.255.252
exit

int se0/0/0
no shut
ip address 10.10.10.26 255.255.255.252
exit
int se0/0/1 
no shut
ip address 10.10.10.38 255.255.255.252
exit

//OSPF
router ospf 10
Auto-cost reference-bandwidth 100000
network 10.10.10.24 0.0.0.3 area 0
network 10.10.10.28 0.0.0.3 area 0
network 10.10.10.36 0.0.0.3 area 0
network 10.10.10.44 0.0.0.3 area 0
network 10.10.10.52 0.0.0.3 area 0
exit
do wr 