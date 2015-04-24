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
FeatureSet1 = zeros(size3,(segsize));
k=1;
while ~feof(fid)  
    currData = fread(fid, segsize);
    if ~isempty(currData)
        A=currData;
        A=A';
        Data = str2num(char(A(:)));
        FeatureSet1(k,:)=Data';
        k=k+1;
    end
end
