#include <string>
#include <cmath>
#include "stdlib.h"
#include <math.h> 

#include <pcl_conversions/pcl_conversions.h>
#include <pcl/filters/statistical_outlier_removal.h>
#include <pcl/point_types.h>
#include <pcl/PCLPointCloud2.h>
#include <pcl/conversions.h>
#include <pcl_ros/transforms.h>
#include <pcl/filters/statistical_outlier_removal.h>
#include "pcl/common/impl/centroid.hpp"	


#include <pcl/ModelCoefficients.h>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include <pcl/sample_consensus/method_types.h>
#include <pcl/sample_consensus/model_types.h>
#include <pcl/segmentation/sac_segmentation.h>


#include <Eigen/Core>
#include <Eigen/Geometry>





//TODO: delete ROS dependencies and adapt code


void detectHandleFromPointCloud(const sensor_msgs::PointCloud2::ConstPtr& msg)
{
  
  if(msg->data.size()>0){

	pcl::PCLPointCloud2* cloud = new pcl::PCLPointCloud2;

	//pcl::PCLPointCloud2ConstPtr cloudPtr(cloud);
	ROS_INFO("saving pcd");

	pcl_conversions::toPCL(*msg, *cloud);
	ROS_INFO("Got points: [%i]", cloud->data.size());

	pcl::PointCloud<pcl::PointXYZ>::Ptr vertices( new pcl::PointCloud<pcl::PointXYZ> );
	pcl::fromPCLPointCloud2(*cloud, *vertices ); 

	ROS_INFO_STREAM("width and height " << vertices->width << " " << vertices->height);




	
	pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_filtered(new pcl::PointCloud<pcl::PointXYZ>);

	for(unsigned i = 0; i < vertices->points.size(); ++i)
  {
    	if ((vertices->points[i].x < 0.1) && (vertices->points[i].x > -0.2) && (vertices->points[i].z < 1.0) && (vertices->points[i].y < 0.3) && (vertices->points[i].y > -0.3) ){

    				if(!std::isnan(vertices->points[i].z) && !std::isnan(vertices->points[i].y) && !std::isnan(vertices->points[i].z) )
    				{

    		    		pcl::PointXYZ p;
    					p.x = vertices->points[i].x;
    					p.y = vertices->points[i].y;
    					p.z = vertices->points[i].z;

    					//ROS_INFO_STREAM("P " << p); 
    					cloud_filtered->points.push_back(p);

					}


    					//ROS_INFO_STREAM("x " << vertices->points[i].x << "y: " << vertices->points[i].y << " z: " << vertices->points[i].z);

    			}


  }


	int count = 0;
	float mean_z = 0.0f;
	bool doIt = true;

for(unsigned i = 0; i < cloud_filtered->points.size(); ++i)
  {


    				if((!std::isnan(cloud_filtered->points[i].z)))
    				{	
    					mean_z = mean_z + vertices->points[i].z;
    					count ++;
    				}


  }
  		mean_z = float(mean_z) / float(count);

 		ROS_INFO_STREAM("Mean z " << mean_z	); 

  		cloud_filtered->height = 1;
  		cloud_filtered->width = cloud_filtered->points.size();


  	pcl::PCDWriter writer1;
    writer1.write<pcl::PointXYZ> ("/tmp/scene.pcd", *cloud_filtered, false);



  	ROS_INFO("Got points for filtered: [%i]", cloud_filtered->points.size());
  	ROS_INFO_STREAM("width and height " << cloud_filtered->width << " " << cloud_filtered->height);



  pcl::ModelCoefficients::Ptr coefficients (new pcl::ModelCoefficients);
  pcl::PointIndices::Ptr inliers (new pcl::PointIndices);
  // Create the segmentation object
  pcl::SACSegmentation<pcl::PointXYZ> seg;
  // Optional
  seg.setOptimizeCoefficients (true);
  // Mandatory
  seg.setModelType (pcl::SACMODEL_PLANE);
  seg.setMethodType (pcl::SAC_RANSAC);
  seg.setDistanceThreshold (0.01);

  seg.setInputCloud (cloud_filtered);
  seg.segment (*inliers, *coefficients);

  if (inliers->indices.size () == 0)
  {
    PCL_ERROR ("Could not estimate a planar model for the given dataset.");
    
  }

  std::cerr << "Model coefficients: " << coefficients->values[0] << " " 
                                      << coefficients->values[1] << " "
                                      << coefficients->values[2] << " " 
                                      << coefficients->values[3] << std::endl;

  std::cerr << "Model inliers: " << inliers->indices.size () << std::endl;


  pcl::PointCloud<pcl::PointXYZ>::Ptr planes(new pcl::PointCloud<pcl::PointXYZ>);


  for (size_t i = 0; i < inliers->indices.size (); ++i){
  						pcl::PointXYZ p;
    					p.x = cloud_filtered->points[inliers->indices[i]].x;
    					p.y = cloud_filtered->points[inliers->indices[i]].y;
    					p.z = cloud_filtered->points[inliers->indices[i]].z;

    					//ROS_INFO_STREAM("P " << p); 
    					planes->points.push_back(p);


    					cloud_filtered->points[inliers->indices[i]].x = -1000;
    					cloud_filtered->points[inliers->indices[i]].y = -1000;
    					cloud_filtered->points[inliers->indices[i]].z = -1000;

  }

	planes->height = 1;
  	planes->width = planes->points.size();


  	pcl::PCDWriter writer2;
    writer2.write<pcl::PointXYZ> ("/tmp/planes.pcd", *planes, false);

  	pcl::PointCloud<pcl::PointXYZ>::Ptr handle(new pcl::PointCloud<pcl::PointXYZ>);


    for(unsigned i = 0; i < cloud_filtered->points.size(); ++i)
  {


    				if( (cloud_filtered->points[i].x != -1000) && (cloud_filtered->points[i].y != -1000) && (cloud_filtered->points[i].x != -1000))
    				{	
    					pcl::PointXYZ p;
    					p.x = cloud_filtered->points[i].x;
    					p.y = cloud_filtered->points[i].y;
    					p.z = cloud_filtered->points[i].z;

    					//ROS_INFO_STREAM("P " << p); 
    					handle->points.push_back(p);
    				}


  }

  	handle->height = 1;
  	handle->width = handle->points.size();


  	pcl::PCDWriter writer3;
    writer3.write<pcl::PointXYZ> ("/tmp/handle.pcd", *handle, false);



    // Create the filtering object
  pcl::StatisticalOutlierRemoval<pcl::PointXYZ> sor;
  pcl::PointCloud<pcl::PointXYZ>::Ptr handle_filtered(new pcl::PointCloud<pcl::PointXYZ>);
  sor.setInputCloud (handle);
  sor.setMeanK (50);
  sor.setStddevMulThresh (1.0);
  sor.filter (*handle_filtered);



  pcl::PCDWriter writer05;
  writer05.write<pcl::PointXYZ> ("/tmp/handle_filtered.pcd", *handle_filtered, false);

  Eigen::Vector4f centroid;
  pcl::compute3DCentroid (*handle_filtered, centroid);


}

}




int main(int argc, char **argv){

//TODO: run code

	return 0;
}
