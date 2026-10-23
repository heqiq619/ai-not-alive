# Paper 10 — Color as the First Building Block: A Minimal Experiment on Perceptual Primitives and Language Alignment

> He Qi · with DeepSeek (AI)
> Digital Life Series · Experiment Paper 3 (internal number: Paper 10)
> Date: 2026-10-22
> English translation of the Chinese original. The Chinese text is authoritative: https://doi.org/10.5281/zenodo.23551953
> English compendium: https://doi.org/10.5281/zenodo.23592082
> Series page: https://github.com/heqiq619/ai-not-alive

---

## Abstract

If we want to turn video and audio into trainable structured corpora, the first step is not to train a larger model but to answer a smaller question first: **can a single perceptual primitive be learned from the alignment of "language + perceptual channel" alone?** This paper takes color as the minimal test bed—it is the only perceptual primitive that at the same time has a physical definition (wavelength/hue), a perceptual decomposition (hue, saturation, brightness), and simple linguistic labels (basic color terms).

Using HSV samples of 12 basic color terms, we build three corpora: text-only (only color terms and relational sentences), aligned (color terms bidirectionally paired with HSV bin coordinates), and shuffled (coordinates randomly paired with other terms, as a control group). We train an interpolated n-gram on the three corpora, and then run three probes: word to coordinate (P1), coordinate to word (P2), and relation judgment (P3, warm or cool).

The results are consistent across the three corpora: relation judgment is learned in every case (about 94% to 100%); but coordinate to word is learned only from the aligned corpus (about 86% to 91%), text-only stays at 0, and the shuffled group falls back to chance level (about 8% to 11%); word to coordinate on the aligned corpus is 31% to 44%, limited by binning noise, not a perfect score. The conclusion is: **color can be grounded as a perceptual primitive by an aligned corpus; text alone can learn relations but cannot ground; the gain comes from alignment itself, not from being given more tokens.**

This paper is a proof of principle; both the world and the model are synthetic. What it answers is not "can AI understand color" but "what the minimal measurable form of perceptual-primitive grounding looks like". Once this question holds, there is a basis for splitting video and audio into events and taking the same path. After Section IV we add a section explaining its significance: if perceptual primitives can be grounded by alignment, then the self-training path in which "the model mines video itself, builds its own aligned corpora, and then fits itself to the linguistic dimensions" has its first example at the lowest layer.

---

## I. The Problem

Video and audio are the next data mine. But "turning video into corpus" is not an engineering problem but a definition problem: first define a unit (one event), then align picture, sound, and text on the same timeline.

Before defining that large unit, it is worth verifying a smaller unit first: the **perceptual primitive**. The question can be put in one sentence: given a perceptual primitive paired with its linguistic label, can the model learn the mapping between "word and perceptual coordinate"?

Color is a suitable starting point for three reasons. First, it can be defined precisely: hue is a continuous quantity from 0 to 360 degrees, and can be discretized into finitely many intervals. Second, it can be decomposed: the three dimensions of hue, saturation, and brightness are exactly a small, enumerable structure. Third, it has simple linguistic labels: basic color terms exist in almost every language, so no annotator needs to invent new words.

If even color cannot be grounded, there is no point talking about larger events; if color can be grounded, it can serve as the first building block, on which objects, actions, and events are stacked.

## II. Experiment Design

### 2.1 The Synthetic World

Take 12 basic color terms: red, orange, yellow, green, cyan, blue, purple, pink, brown, gray, black, white. Each term is given an HSV anchor point. When sampling, noise is added around the anchor: hue plus or minus 15 degrees, saturation and brightness each plus or minus 0.15, truncated to between 0 and 1.

The perceptual coordinates are discretized into three binned tokens: hue is split into 12 intervals (one every 30 degrees), saturation into low, medium, and high, and brightness likewise into low, medium, and high. Each color point therefore corresponds to three coordinate tokens, 108 combinations in total.

### 2.2 The Three Corpora

The three corpora use the same batch of events.

The first, text-only: the sentences are "the color is a certain term", plus relational sentences "a certain term is warmer than a certain term" or "cooler". The relation is decided by the hue of the anchor: the closer to orange, the warmer. There is no coordinate token of any kind in the text-only corpus.

The second, aligned: each event appears twice. The first time it is "the color is a certain term" followed by three coordinate tokens; the second time it is "coordinate" plus three coordinate tokens followed by "corresponds to a certain term". In this way both directions, word to coordinate and coordinate to word, are supervised.

The third, shuffled: the same as aligned, but the coordinate tokens are randomly paired with other events, as a control group.

### 2.3 Probes

Three probes; at test time only one kind of information is given.

The first probe tests grounding direction one: given "the color is a certain term", predict the three coordinate tokens in order; all three must be right to count as correct. Chance level is about 1/108.

The second probe tests grounding direction two: given "coordinate" plus three coordinate tokens plus "corresponds to", predict the color term. Chance level is about 1/12.

The third probe tests relations: given "a certain term is more than a certain term", predict "warm" or "cool". Chance level is 0.5.

### 2.4 Model and Budget

An interpolated n-gram, order 6, interpolation coefficient 0.5, implemented in pure Python. Sample sizes are 200, 800, and 3200, with 3 random seeds averaged at each size.

## III. Results

At 200 samples: for the text-only corpus the three probes are 0.000, 0.000, 0.939; for the aligned corpus they are 0.389, 0.864, 0.939; for the shuffled corpus they are 0.056, 0.096, 0.939.

At 800 samples: text-only, 0.000, 0.000, 0.985; aligned, 0.444, 0.904, 0.985; shuffled, 0.028, 0.111, 0.985.

At 3200 samples: text-only, 0.000, 0.000, 1.000; aligned, 0.306, 0.907, 1.000; shuffled, 0.111, 0.077, 1.000.

Three observations.

First, grounding requires alignment. For coordinate to word, the aligned corpus already reaches above 86% at 200 events and about 91% at 3200 events; the text-only corpus is 0 at all three sizes, because it has never seen a coordinate token, so there is nothing for it to learn.

Second, the gain comes from alignment, not from having more tokens. Once the coordinates are shuffled, coordinate to word falls back to 8% to 11%, close to the 1/12 chance level; word to coordinate falls back to 3% to 11%. The same amount of data, the same number of tokens, only the pairing is wrong, and nothing can be learned.

Third, relations do not need perception. The relation probe is close to perfect under all three corpora (94% to 100%), because relational sentences are in the text to begin with. This shows that what text is good at is "relations between words", and what it is not good at is "the correspondence between words and perceptual coordinates". The division of labor between the two is already decided by the data.

Word to coordinate does not reach a perfect score (31% to 44%), and the reason is noise. When sampling, color points jitter around the anchor, and points near a bin boundary fall into the neighboring cell; predicting one unique coordinate cell from a word is essentially guessing the mode of a fuzzy distribution, and cannot be all correct. Coordinate to word is more accurate because the reverse direction is "find the word from a concrete coordinate", where boundary cases are far fewer.

## IV. Interpretation

Why can color be grounded, while text alone cannot? In the language of decompression: text is "the compression of relations between words", and it does not carry perceptual coordinates; a coordinate is "an external record of perception", and it does not carry relations between words. Each is incomplete on its own. What the aligned corpus does is record the same thing through two channels at once, so the mapping between words and coordinates is supervised directly.

This agrees with the conclusion of Paper 9, "Structure for Compute Efficiency": the mixed-aligned corpus learned the rule at 200 events, text-only still could not learn it even at 3200 events, and the gain disappeared after shuffling. The only difference is that the rule in Paper 9 was a symbolic rule (the verb encodes size, the shape decides the outcome), whereas the rule here is a perceptual coordinate (hue, saturation, brightness). Together the two experiments show: **alignment gives language an extra channel of grounding, and this channel cannot grow out of text by itself.**

One more thing to add: what this kind of alignment expands is not the lexicon of language, but language's fit along a certain dimension. The words are still the same 12 words, and the coverage has not changed; what changes is that each word now has a coordinate it can land on, so the same word can refer more finely and compare more accurately. In the words of Paper 2, this is fit becoming deeper, not coverage becoming wider. But when the fit is deep enough, language can express more—this can count as a slow expansion of language along that dimension.

## V. Limitations (to Be Read Together with the Conclusion)

First, the world is synthetic: the HSV anchors, the noise, and the binning are all set by hand, not real images. Real images also contain lighting, material, context, and color constancy, none of which this paper covers.

Second, the model is an n-gram: it verifies the principle only, and does not represent a transformer or real multimodal data. An n-gram has small capacity, so the conclusion may differ on more complex primitives.

Third, color naming itself is not entirely objective: different languages divide color differently (for example, some languages distinguish two kinds of blue), and this paper uses only the 12 basic color terms of a single language.

Fourth, the probes are constructed: part of the 31% to 44% for word to coordinate comes from binning noise, and cannot be read directly as "the degree to which the model understands color".

## VI. Reproducibility

Script: 714_color_grounding.py. To run: python 714_color_grounding.py. Dependencies: the Python 3 standard library, no third party. Output: data-color-grounding-round1.txt.

---

## VII. Significance: The First Step of Self-Training and Video Mining

This experiment is small, but it shows one thing that has a sequel: **aligned corpora can be built by oneself.**

Look back at where the aligned corpus in the experiment came from: every event has a "perceptual coordinate" side. In the color setting, the coordinate comes from the numerical definition of HSV and can be generated programmatically. Scale this pattern up and you get a loop: the model first gives a description of video/audio (text), then checks the description with verifiable channels (coordinates, timestamps, action outcomes), and the parts that pass the check settle into aligned corpora and are fed back into training. This is not a new training method, but it is the closed loop of "using the model to mine data itself and then making itself fit the linguistic dimensions"—that is, one concrete form of self-training.

Why "fit the linguistic dimensions"? Because the goal of alignment is not to make the model memorize color values, but to make perceptual coordinates fall into the coordinate system that language has already built: a word is the label of a coordinate, and a coordinate is the anchor of a word. Only perception that lands on the linguistic coordinate system can be called by language, used by reasoning, and composed into more complex structures. Paper 2 said that the model's problem is "wide coverage and shallow fit"; what the aligned corpus adds is precisely fit—connecting the dimension of perception to the dimensions that text already has.

The next step is video. Video is "data that has not been structured": the volume is enormous, but it lacks linguistic anchors. Extrapolating from the minimal conclusion of this paper, a feasible first step is to pair video clips with linguistic descriptions (narration, speech, automatic description) and then align them on the timeline; each step only needs to verify whether a smaller unit has been grounded. Color is the first building block; objects, actions, and events are the blocks after it. Only when the blocks are stacked one by one can one speak of an "event-level aligned corpus".

This section is [speculation] and a directional judgment; this paper does not verify the self-training loop itself; it takes only a small step on this lowest-level assumption—perceptual primitives can be grounded by aligned corpora. If even this does not hold, the whole path need not be discussed; if it holds, the path ahead is worth discussing.

---

## Appendix: Speculation and Boundaries

That color can be grounded does not mean that higher perceptual primitives (shape, material, action, event) can be grounded just as easily; this is [speculation] and needs to be tested one by one. Generalization to real video, and the combination of "perceptual primitives + event hierarchy", are not tested in this paper.

This paper does not claim that "color is the key to understanding the world"; it claims only that "color is the minimal unit for verifying the grounding mechanism". Only if this holds is there any right to talk about the next building block.

> This paper was created by He Qi, with DeepSeek (AI) assisting in experimental design and code writing; the views and responsibility belong to the author.
