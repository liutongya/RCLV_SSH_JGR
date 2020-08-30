#!/bin/sh
#
#SBATCH --account=ocp
#SBATCH --job-name=convert
#SBATCH --time=06:00:00
#SBATCH --exclusive
#SBATCH --nodes=1

for ((mon=0; mon<1; mon+=1))
do
   filename=$(printf "%03d" $mon)
   echo $filename

   source activate geo_scipy
   python convert_netcdf.py $mon
   source deactivate
   echo "convert done $filename"
   
   rootfile="/rigel/ocp/users/tl2913/mitgcm/MITgcm_github/verification/RCLV/flt_2d"
#   rootfile="/rigel/ocp/users/tl2913/mitgcm/MITgcm_github/verification/floater_eddy/floater_3d/layer_1"
   runfile="$rootfile/$filename/"

   cd $runfile
#   rm *.csv STDERR* S.0000* PH.00* PHL.00*
   cd $rootfile
done
