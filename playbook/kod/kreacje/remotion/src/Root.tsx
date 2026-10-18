import React from 'react';
import { Composition } from 'remotion';
import { Szukanie } from './Szukanie';
import { Audyt } from './Audyt';
export const Root: React.FC = () => (<>
  <Composition id="szukanie" component={Szukanie} durationInFrames={450} fps={30} width={1080} height={1920} />
  <Composition id="audyt" component={Audyt} durationInFrames={420} fps={30} width={1080} height={1920} />
</>);
