clc;
clear all;
!C:\Python27\pythonw.exe MergeFiles.py fs_remainingWords_1gm_trng Trainingtweets_without_RT_final_prune
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
RES_M=zeros(m,n);
fs_remainingWords_1gm_trng_ma=ones(n,1)-fs_remainingWords_1gm_trng;
for i = 1:m
    RES(i,:) = featureSet_1(i,:) .* fs_remainingWords_1gm_trng';
    RES_M(i,:) = featureSet_1(i,:) .* fs_remainingWords_1gm_trng_ma';
end
countFem=0;
for i=1:m
    if(Labels(i,1)==2)
        countFem=countFem+1;
    end
end
Fem_prob=countFem/m;
Male_prob=1-Fem_prob;
for i = 1:m
    p_male=1;
    p_female=1;
    for j=1:n
        if(RES(i,j)>0)
            p_female = p_female*RES(i,j);
        end
        if(RES_M(i,j)>0)
            p_male = p_male*RES(i,j);
        end
    end
    prob_male(i,1)=p_male;
    prob_female(i,1)=p_female;
end

prob_test_m = prob_male*Male_prob;
prob_test_fm=prob_female*Fem_prob;
label_test=ones(m,1);
for i=1:m
    if prob_test_fm(i,1)>=prob_test_m(i,1)
        label_test(i,1)=2;
    end
end
countMatch=0;
for j=1:m
    if label_test(j,1) == Labels(j,1)
        countMatch=countMatch+1;
    end
end
accuracy = countMatch/m