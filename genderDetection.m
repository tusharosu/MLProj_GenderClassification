clc;
clear all;
%!C:\Python27\pythonw.exe MergeFiles.py fs_remainingWords_1gm_trng Testingtweets_without_RT_final_prune
fs_remainingWords_1gm_trng=importdata('fs_remainingWords_1gm_trng_probablility.txt');
Testingtweets_pruned = importdata('Testingtweets_without_RT_final_prune.txt');
probability_words = importdata('fs_remainingWords_1gm_trng.txt');
probability_words = probability_words.data(:,2);
[size1,size2]=size(fs_remainingWords_1gm_trng);
[size3,size4]=size(Testingtweets_pruned);
fid = fopen( 'fs_remainingWords_1gm_trng_featureSet.txt', 'r' ) ;
segsize = size1+1;
featureSet_temp = zeros(size3,(segsize));
k=1;
while ~feof(fid)
    currData = fread(fid, segsize);
    if ~isempty(currData)
        A=currData';
        featureSet_temp(k,:)=A;
        k=k+1;
    end
end
featureSet_temp=featureSet_temp - 48;
featureSet_1 = featureSet_temp(:,1:size1);
Labels= featureSet_temp(:,size1+1);

n = size(featureSet_1,2);
m = size(featureSet_1,1);
RES = zeros(m,n);

for i = 1:m
    RES(i,:) = featureSet_1(i,:) .* fs_remainingWords_1gm_trng';
end

prob_test = RES*probability_words;
label_test=ones(m,1);
for i=1:m
    if prob_test(i,1)>=0.5
        label_test(i,1)=2;
    end
end
countMatch=0;
for j=1:m
    if label_test(i,1) == Labels(i,1)
        countMatch=countMatch+1;
    end
end
accuracy = countMatch/m