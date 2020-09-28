# LiDAR and 3D Point Cloud Task types and applications

It's a overview and working notes to get LiDAR applications, cloud solutions, open datasets, and state of arts research papers.

Summarize the application scopes:

* 3D model reconstruction
* Geometry / Localization
* 3D object detection
* 3D object tracking
* 3D semantic segmentation
* Safty & Security: people or object comming into a place.

Image source: Deep Learning for 3D Point Clouds: A Survey, Yulan Guo [link](https://arxiv.org/pdf/1912.12033.pdf) 
![](https://raw.githubusercontent.com/QingyongHu/SoTA-Point-Cloud/master/taxonomy.png)

## Data process and visulization
#### 1. Raw Data of Point Cloud

* 3D Point Clouds: (x, y, z, i, r, g, b)
	* Three coordinates: x, y, and z.
	* Intensity: i
	* Color: red (r), green (g), and blue (b) 8-bit color channels.

* Coordinate systems and sensor fusion

	Applications: global path planning, localization, mapping, and driving scenario simulations.
	
	World coordiante system (WCS): 1. two sensors with different point clouds data. 2. Translate all point cloud frames into a single coordinate system.
	
	
	* Vehicle Axis System(VAS)[ISO 8855](https://www.iso.org/standard/51180.html): x axis is forward toward the car’s movement, y axis is left, and the z axis points up from the ground.

	![](https://upload.wikimedia.org/wikipedia/commons/f/f5/RPY_angles_of_cars.png)
	
	* GPS/IMU - OxTS in AV KITTI dataset
		*  (latitude, longitude, altitude and roll, pitch, yaw)

		![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Flight_dynamics_with_text_ortho.svg/1920px-Flight_dynamics_with_text_ortho.svg.png)[By Aashmango4793 - Own work, CC BY-SA 4.0](https://commons.wikimedia.org/w/index.php?curid=81688701)
		
	### Compare OxTS and VAS ISO 8855 
	Notes: the Z-axis direction is different
	
	![](https://www.oxts.com/wp-content/uploads/2016/01/555_ISO8855_ISO70000.jpg)


#### 2. Processed Point Cloud

* Coordinate systems 
* Conversion to 3D surfaces: polygon mesh, triangle mesh, CAD models.
* Building Information Model (BIM): 3D or 2D. Generating or reconstructing 3D shapes from single or multi-view depth maps or silhouettes and visualizing them in dense point clouds.

![Wiki Synthesize 3D](https://upload.wikimedia.org/wikipedia/commons/6/6d/Synthesizing_3D_Shapes_via_Modeling_Multi-View_Depth_Maps_and_Silhouettes_With_Deep_Generative_Networks.png)

* GIS - Digital elevation model [DEM](https://en.wikipedia.org/wiki/Digital_elevation_model) [USGS](https://www.usgs.gov/faqs/what-are-digital-elevation-models-dems?qt-news_science_products=0#)

![Wiki 3D Rendering DEM](https://upload.wikimedia.org/wikipedia/commons/f/ff/Mtm-05277e_3d.png)
	
#### 3. Visulized Point Cloud


## Analytic and ML cases
* 3D point cloud object detection
* 3D point cloud object tracking
* 3D point cloud semantic segmentation


## LiDAR Technology Overview
* LiDAR Tech Stock [link](https://spationetblog.files.wordpress.com/2016/01/an-introduction-to-lidar-technology.pdf)

## AWS
* Labeling data for 3D object tracking and sensor fusion [link](https://aws.amazon.com/blogs/machine-learning/labeling-data-for-3d-object-tracking-and-sensor-fusion-in-amazon-sagemaker-ground-truth/)

## Apple
* Acess to the point cloud/mesh created by LiDAR with the new Ipad Pro [Link](https://developer.apple.com/forums/thread/131161) Currently, Apple ARKit don't provide simple way to export cloud points. Need to use ARKit to retrieve geometry object. Require iOS 13.4+ and Xcode 11.4+.

* Sample Code
	* Visualizing and Interacting with a Reconstructed Scene [link](https://developer.apple.com/documentation/arkit/world_tracking/visualizing_and_interacting_with_a_reconstructed_scene)
	* WWDC2020 ARKit4 [link](https://developer.apple.com/videos/play/wwdc2020/10611/) Sample code [link](https://developer.apple.com/documentation/arkit/visualizing_a_point_cloud_using_scene_depth)

## Machine Learning
* OpenPCDet [repo](https://github.com/open-mmlab/OpenPCDet)

### Papers
* **Deep Learning for 3D Point Clouds: A Survey** IEEE 2020 A good start point, including papers, datasets, and metrics. [link](https://arxiv.org/pdf/1912.12033.pdf) [github](https://github.com/QingyongHu/SoTA-Point-Cloud)
* Deep Learning for 3D Point Cloud Understanding: A Survey [link](https://arxiv.org/pdf/2009.08920.pdf) [github](https://github.com/SHI-Labs/3D-Point-Cloud-Learning)
* Deep Learning for LiDAR Point Clouds in Autonomous Driving: A Review IEEE 2020 [link](https://arxiv.org/pdf/2005.09830.pdf)
* PV-RCNN: Point-Voxel Feature Set Abstraction for 3D Object Detection. [CVPR 2020](https://openaccess.thecvf.com/content_CVPR_2020/papers/Shi_PV-RCNN_Point-Voxel_Feature_Set_Abstraction_for_3D_Object_Detection_CVPR_2020_paper.pdf)

## LiDAR datasets
* KITTI cvlibs [link](http://www.cvlibs.net/datasets/kitti/)
* A2D2 Audi Autonomous Driving Dataset on AWS [link](https://registry.opendata.aws/aev-a2d2/)
* NuScenes [link](https://www.nuscenes.org/)

## Devices

* Robotis LDS-01 [link](https://emanual.robotis.com/docs/en/platform/turtlebot3/appendix_lds_01/)