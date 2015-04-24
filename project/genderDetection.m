clc;
clear all;

%!C:\Python27\pythonw.exe MergeFiles.py fs_remainingWords pruned_final_onlywords

fs_remainingWords=importdata('fs_remainingWords_probablility.txt');
pruned_final_onlywords = importdata('pruned_final_onlywords.txt');
[size1,size2]=size(fs_remainingWords);
[size3,size4]=size(pruned_final_onlywords);

fid = fopen( 'fs_remainingWords_featureSet.txt', 'r' ) ;
%tline = fgetl(fid);
%C=textscan(fileID,'%s');
%A=zeros(size3,size1+1);
%
% while 1
%   tline = fgetl(fid);
%   if ~ischar(tline), break, end
%   A(row, :) = str2double(regexp(tline, ' ', 'split'));
% end
% fclose(fid);
segsize = size1+1;
FS1 = zeros(size3,(segsize));
k=1;
while ~feof(fid)
    currData = fread(fid, segsize);
    if ~isempty(currData)
        A=currData';
        FS1(k,:)=A;
        k=k+1;
    end
end
FS1=FS1 - 48;
FeatSet1 = FS1(:,1:size1);
Labels= FS1(:,size1+1);

n = size(FeatSet1,2);
m = size(FeatSet1,1);
RES = zeros(m,1);

for i = 1:m
    TEMP = FeatSet1(i,:) .* fs_remainingWords';
    pr = 1.0;
    for j = 1:size(TEMP,2)
        if TEMP(1,j) > 0
            pr = pr * TEMP(1,j);
        end
    end
    RES(i,1) = pr;
end