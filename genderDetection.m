clear all;
%!C:\Python27\pythonw.exe MergeFiles.py fs_remainingWords Testingtweets_without_RT_final_prune
fs_remainingWords=importdata('fs_remainingWords_probablility.txt');
Testingtweets_pruned = importdata('Testingtweets_without_RT_final_prune.txt');
[size1,size2]=size(fs_remainingWords);
[size3,size4]=size(Testingtweets_pruned);
fidfs = fopen( 'fs_remainingWords_featureSet.txt', 'r' ) ;
segsizefs = size1+1;
FeatureSetforfs_1_temp = zeros(size3,(segsizefs));
k=1;
while ~feof(fidfs)
    currData = fread(fidfs, segsizefs);
    if ~isempty(currData)
        A=currData';
        FeatureSetforfs_1_temp(k,:)=A;
        k=k+1;
    end
end
FeatureSetforfs_1_temp=FeatureSetforfs_1_temp - 48;
FeatureSet_1 = FeatureSetforfs_1_temp(:,1:size1);
Labels= FeatureSetforfs_1_temp(:,size1+1);