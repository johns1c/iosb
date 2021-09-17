# lists backups and the details 
# an test example of how to read iTunes made backups of iOS devices on a Windows machine
#  Chris Johnson
#
from biplist import *
import plistlib 
import sqlite3 
import sys
import glob
import os
import pprint
import datetime
manifest_db = r'c:\users\Chris Johnson\AppData\Roaming\Apple Computer\MobileSync\backup\25c62f1f692d84eca07462a1f33785ba58000b6d\Manifest.db' 
manifest = 'Status.plist' 
if len(sys.argv) > 1 :
    manifest = sys.argv[1] 
    
def rbp(  manifest)    : 
    try:
        plist = readPlist(manifest)
        print( dict([(k , f'{plist[k]}' ) for k in sorted(plist)])  ) 
    except (InvalidPlistException, NotBinaryPlistException)as e:
        print ( "Not a plist :", e )
    
def rip(  ifile ) :

    try:
        plist = plistlib.load(open(ifile,'rb'))
        
        wanted = ['Build Version', 'Device Name', 'Display Name', 'GUID', 'ICCID', 'IMEI',
        'Last Backup Date', 'MEID', 'Phone Number', 'Product Name', 'Product Type',
        'Product Version', 'Serial Number', 'zzzSync Settings', 'Target Identifier',
        'Target Type', 'Unique Identifier', 'zziTunes Files', 'zzziTunes Settings', 
        'iTunes Version']
        
        [ print ( k , plist[k] ) for k  in plist if k in wanted ]

        #plist = biplist.load(fp, fmt="FMT_XML")
        import pdb
        pdb.set_trace()
    except (plistlib.InvalidFileException)as e:
        print ( "info.plist Not an xml  plist :", e )
    
def part1(  input :str ) :
        return   input.split( '-' )[0] 
       
    
path = "C:\\Users\\*\\AppData\\Roaming\\Apple Computer\\MobileSync\\Backup\\*"
all_paths = glob.glob(path)

for f in all_paths :

    spl = os.path.join( f , 'Status.plist' )
    ipl = os.path.join( f , 'Info.plist' ) 
    
    
    
    if os.path.exists( spl) :
        try:
            print( f'============== {f} ==================' ) 
            rbp( spl )
        except:
            print( '?' * 50 ) 
            
    if os.path.exists( ipl ) :
            rip( ipl ) 

    manifest = os.path.join( f , 'Manifest.db' ) 
    old_manifest = os.path.join( f , 'Manifest.mbdb' ) 
    
    if os.path.exists( old_manifest ) :
        print( 'old manifest' ) 
    elif os.path.exists( manifest) :
        db = sqlite3.connect(manifest)
        db.create_function("part1", 1, part1)
        qry = 'select distinct part1( domain ) from files order by 1 ; '
        cur = db.cursor()
        cur.execute(qry) 
        for row in cur.fetchall() :
            print( row) 
            
        # pull sample file 

        qry = "select * from files where RelativePath like '%Naomi%zip' ;"
        cur.execute(qry) 
        for row in cur.fetchall() :
            print( row[:4]) 
            props = row[4 ] 
            print ( f'----------------------------props ' )
            #print( props )
            
            from io import BytesIO
            with BytesIO(props) as props_f:
                props_plist = readPlist( props_f ) 
                
                zu = props_plist['$objects'][1]['LastModified']
                zs = props_plist['$objects'][1]['LastStatusChange']
                zc = props_plist['$objects'][1]['Birth']
                
                zu =  datetime.datetime.utcfromtimestamp(zu).isoformat()
                zs =  datetime.datetime.utcfromtimestamp(zs).isoformat()
                zc =  datetime.datetime.utcfromtimestamp(zc).isoformat()
                
                props_plist['$objects'][1]['LastModified']  = zu
                props_plist['$objects'][1]['LastStatusChange'] = zs
                props_plist['$objects'][1]['Birth'] = zc
                
                
                pprint.pprint( props_plist) 
        
        print( f'{manifest} does not exist ' ) 
     
     
     