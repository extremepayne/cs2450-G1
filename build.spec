a = Analysis(
    ['src/run_gui.py'],
    pathex=[os.path.abspath('.')],
    binaries=[],
    datas=[
        ('src/gui/assets', 'src/gui/assets'),
        ('courses.json', '.'),
        ('tasks.json', '.'),
    ],
    hiddenimports=[
        'tkinter',
        'tkcalendar',
        'src.course',
        'src.task',
        'src.gui.gui',
        'src.gui.components'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='TaskManager',     
    debug=False,            
    strip=False,            
    upx=True,              
    console=False,          
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

# macOS specific
app = BUNDLE(
    exe,
    name='TaskManager.app',
    icon=None,  # Remove icon reference if not available
    bundle_identifier='com.taskmanager.app',
)