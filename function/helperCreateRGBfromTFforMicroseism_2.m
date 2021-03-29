% 使用matlab运行可以补充enhance_data_4的数据扩充，python调用matlab无法完成这一点
function helperCreateRGBfromTFforMicroseism_2(parentFolder,childFolder)
%parentFolder = 'L:\dataset_for_graduation'
%childFolder = 'Microseism'
% This function is only intended to support the ECGAndDeepLearningExample.
% It may change or be removed in a future release.
Fs = 10000;
imageRoot = fullfile(parentFolder,childFolder);
datadir = pwd();
datafile = dir(fullfile(datadir,'*.mwf'));
for i = 1 : length(datafile)
data = importdata(datafile(i).name);
[~,x] = size(data.data);
if x > 2
    data = data.data(:,1) + data.data(:,2) + data.data(:,3);
else
    data = data.data;
end


change_data = [data(1:1000);data(1:1000);data(1:1000);data(1:1000);data];
y = WienerScalart96(change_data,Fs,0.7);
y = y(4001:end);
data = y;

signalLength = length(data(:,1));
fb = cwtfilterbank('SignalLength',signalLength,'SamplingFrequency',Fs,'VoicesPerOctave',12);

[cfs,~] = wt(fb,data);
cfs = abs(cfs);
im = ind2rgb(im2uint8(rescale(cfs)),jet(128));
imgLoc = fullfile(imageRoot);
imFileName = strcat('Microseism_enhance_data_4_',datafile(i).name(1:end-4),'.jpg');
imwrite(imresize(im,[224 224]),fullfile(imgLoc,imFileName));
end
end