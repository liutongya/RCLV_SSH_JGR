#!/bin/sh

#SBATCH --account=ocp
#SBATCH --job-name=RCLV
#SBATCH --time=24:00:00
#SBATCH --exclusive
#SBATCH -N 12

#echo "run for floater"
for ((mon=20; mon<25; mon+=1))
do
#    step=`expr $mon \* $dt`
#    echo "step: $step"    
    mon_next=`expr $mon + 1`    
    filename=$(printf "%03d" $mon_next)
    echo $filename    
    if [ ! -d $filename ]; then
        mkdir $filename
        echo "created $filename"
    fi

    rootfile="/rigel/ocp/users/tl2913/mitgcm/MITgcm_github/verification/RCLV/flt_2d"
    datafile="$rootfile/tmpfile/*"
    runfile="$rootfile/$filename/"
    floaterfile="$rootfile/tmpfile/*floater.bin"
    rm -f $floaterfile
# python
    source activate geo_scipy
    mpirun python copy_files_to_local_dir.py
    python make_initial_files.py $mon
    source deactivate

#    echo $runfile
    cp $datafile $runfile
    echo "copy completed for $filename"
# run the model
    cd $runfile
#    module add intel-parallel-studio/2017 netcdf-fortran/4.4.4 netcdf/gcc/64/4.4.0
    echo "Running MITgcm in $runfile"
    mpirun -n 288 ./mitgcmuv
    cd $rootfile
# convert data
    python convert_netcdf.py $mon
    echo "convert done in $filename"
    cd $runfile
    rm -f float_trajectories*.csv S.0000* STD* *pickup*
    cd $rootfile 
done

