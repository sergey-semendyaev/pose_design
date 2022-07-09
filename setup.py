from setuptools import setup

package_name = 'pose_design'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ivan',
    maintainer_email='smirnov.ie@phystech.edu',
    description="Design poses of robot Nao",
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
               'pose_design = pose_design.PoseDesign:main'
        ],
    },
)
