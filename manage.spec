# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['manage.py'],
             pathex=['D:\\WorkSpace\\PycharmProject\\database'],
             binaries=[],
             datas=[
                 (r'D:\WorkSpace\PycharmProject\database\templates', r'.\templates'),
                 (r'D:\WorkSpace\PycharmProject\database\static', r'.\static'),
                 (r'D:\WorkSpace\PycharmProject\database\media', r'.\media'),
                 (r'D:\Software\Anaconda3\envs\web2\Lib\site-packages\simpleui', r'.\simpleui'),
                 ],
             hiddenimports=['simpleui.apps', 'redwood.apps', 'redwood.admin'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='manage',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='manage')
