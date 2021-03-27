
% function helperCreateRGBfromTFforMicroseism(parentFolder,childFolder,label)
% % This function is only intended to support the ECGAndDeepLearningExample.
% % It may change or be removed in a future release.
% Fs = 10000;
% imageRoot = fullfile(parentFolder,childFolder);
% datadir = pwd();
% datafile = dir(fullfile(datadir,'*.mwf'));
% for i = 1 : length(datafile)
% data = importdata(datafile(i).name);
% [~,x] = size(data.data);
% if x > 2
%     data = data.data(:,1) + data.data(:,2) + data.data(:,3);
% else
%     data = data.data;
% end
% signalLength = length(data(:,1));
% 
% fb = cwtfilterbank('SignalLength',signalLength,'SamplingFrequency',Fs,'VoicesPerOctave',12);
% 
% [cfs,~] = wt(fb,data);
% cfs = abs(cfs);
% im = ind2rgb(im2uint8(rescale(cfs)),jet(128));
% imgLoc = fullfile(imageRoot,label);
% imFileName = strcat(label,'_',num2str(i),'.jpg');
% imwrite(imresize(im,[224 224]),fullfile(imgLoc,imFileName));
% end
% end


function helperCreateRGBfromTFforMicroseism(signal,filename,label)

save_path = 'G:\dataset_for_graduation';
Fs = 10000;
signalLength = length(signal);

fb = cwtfilterbank('SignalLength',signalLength,'SamplingFrequency',Fs,'VoicesPerOctave',12);
[cfs,~] = wt(fb,signal);
cfs = abs(cfs);
im = ind2rgb(im2uint8(rescale(cfs)),jet(128));
imgLoc = fullfile(save_path,label);
imFileName = strcat(label,'_',filename,'.jpg');
imwrite(imresize(im,[224 224]),fullfile(imgLoc,imFileName));

end


