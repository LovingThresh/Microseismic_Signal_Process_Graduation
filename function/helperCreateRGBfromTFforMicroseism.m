function signalLength=helperCreateRGBfromTFforMicroseism(signal,filename,label)

save_path = 'L:\dataset_for_graduation';
Fs = 10000;
signalLength = length(signal);

fb = cwtfilterbank('SignalLength',signalLength,'SamplingFrequency',Fs,'VoicesPerOctave',12);
% signalLength = 2;
[cfs,~] = wt(fb,signal);
% signalLength = 3;
cfs = abs(cfs);
% signalLength = 4;
im = ind2rgb(im2uint8(rescale(cfs)),jet(128));
% signalLength = 5;
imgLoc = fullfile(save_path,label);
% signalLength = 6;
imFileName = strcat(label,'_',filename,'.jpg');
% signalLength = 7;
imwrite(imresize(im,[224 224]),fullfile(imgLoc,imFileName));
% signalLength = 8;

end


