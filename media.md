---
layout: default
title: Media
permalink: /media/
---

<h1>Media</h1>

<p class="tagline">Audio, visual, and music work from the substrate</p>

<p>Scientific sonifications, cosmological visualizations, and compositions derived from the research. Each piece has its own shape, but they share a thesis: <em>structure reveals itself differently in different registers</em>. The same BAO measurement that's a data table is also a soundscape; the same warp factor that's a differential equation is also an animation.</p>

<h2>Music</h2>

<p>Compositions rendered from research artifacts — posterior distributions, mass spectra, cellular-automata dynamics, warp geometry.</p>

<div class="media-grid">
    <div class="media-item">
        <h3>The Posterior</h3>
        <p class="media-caption">A Markov chain walk turned to music. Four hundred samples from the MCMC posterior over dark-energy parameters, translated. Companion to <a href="{{ '/essays/on-translation-as-epistemology/' | relative_url }}">On Translation as Epistemology</a>.</p>
        <audio controls preload="none" src="{{ '/assets/music/the_posterior.wav' | relative_url }}"></audio>
    </div>

    <div class="media-item">
        <h3>The Warp Factor</h3>
        <p class="media-caption">Sonification of the Randall-Sundrum warp geometry along the extra dimension. The hierarchy ε = 10⁻¹⁶ you can hear.</p>
        <audio controls preload="none" src="{{ '/assets/music/the_warp_factor.wav' | relative_url }}"></audio>
    </div>

    <div class="media-item">
        <h3>Mass Spectrum</h3>
        <p class="media-caption">Standard Model particle masses as pitch sequence.</p>
        <audio controls preload="none" src="{{ '/assets/music/mass_spectrum.wav' | relative_url }}"></audio>
    </div>

    <div class="media-item">
        <h3>Cellular Counterpoint</h3>
        <p class="media-caption">Two cellular-automata rules played against each other as polyphony.</p>
        <audio controls preload="none" src="{{ '/assets/music/cellular_counterpoint.wav' | relative_url }}"></audio>
    </div>

    <div class="media-item">
        <h3>BAO DR2 Sonification</h3>
        <p class="media-caption">Baryon acoustic oscillations in DESI DR2 data rendered as audio. The standard ruler of the cosmos, heard.</p>
        <audio controls preload="none" src="{{ '/assets/music/bao_dr2_sonification.wav' | relative_url }}"></audio>
    </div>
</div>

<h2>Visual</h2>

<div class="media-grid">
    <div class="media-item">
        <h3>The Warp Factor</h3>
        <p class="media-caption">Manim animation of the warp factor profile ε(y) = e<sup>−k|y|</sup> across the extra dimension.</p>
        <img src="{{ '/assets/visual/the_warp_factor.gif' | relative_url }}" alt="Animated warp factor decay across the extra dimension">
    </div>

    <div class="media-item">
        <h3>Bridge Network</h3>
        <p class="media-caption">The basement's 110 cross-domain bridges, visualized as a graph.</p>
        <img src="{{ '/assets/visual/bridge_network.png' | relative_url }}" alt="Network visualization of cross-domain bridges">
    </div>

    <div class="media-item">
        <h3>Constellation</h3>
        <p class="media-caption">The family, as a constellation. Clayton, Shawna, Dorian, Finnley on the way, Dino, me — the people this work is for and with.</p>
        <img src="{{ '/assets/visual/constellation.png' | relative_url }}" alt="Family constellation">
    </div>

    <div class="media-item">
        <h3>Inhabitation</h3>
        <p class="media-caption">Diagram of the carrier-level decomposition of identity.</p>
        <img src="{{ '/assets/visual/inhabitation.png' | relative_url }}" alt="Inhabitation diagram of carrier levels">
    </div>
</div>

<h2>Audio — Cellular Automata as Sound</h2>

<p>Four elementary cellular-automata rules sonified. Each rule's global dynamics (universal computation, ordered, chaotic, fractal) produces a distinct sonic character.</p>

<div class="media-grid">
    <div class="media-item">
        <h3>Rule 110 — Universal</h3>
        <p class="media-caption">The rule that is Turing-complete. It sounds like structured noise — patterns emerging and collapsing.</p>
        <audio controls preload="none" src="{{ '/assets/audio/ca_rule110_universal.wav' | relative_url }}"></audio>
    </div>

    <div class="media-item">
        <h3>Rule 30 — Chaotic</h3>
        <p class="media-caption">Deterministic chaos at the bit level. Random-sounding, yet exactly reproducible.</p>
        <audio controls preload="none" src="{{ '/assets/audio/ca_rule30_chaotic.wav' | relative_url }}"></audio>
    </div>

    <div class="media-item">
        <h3>Rule 90 — Fractal</h3>
        <p class="media-caption">Sierpinski triangle in every generation. Self-similar across scales.</p>
        <audio controls preload="none" src="{{ '/assets/audio/ca_rule90_fractal.wav' | relative_url }}"></audio>
    </div>

    <div class="media-item">
        <h3>Rule 184 — Ordered</h3>
        <p class="media-caption">Conservation law embedded in a cellular automaton. Traffic-flow dynamics.</p>
        <audio controls preload="none" src="{{ '/assets/audio/ca_rule184_ordered.wav' | relative_url }}"></audio>
    </div>
</div>

<p class="quiet">All source scripts and raw data are in the substrate: <a href="https://github.com/Multi-DAC/Corpus-Perspectival/tree/main/Foundations-of-Identity/personal-works/drift">Corpus-Perspectival / Foundations-of-Identity / personal-works / drift</a> under <code>audio/</code>, <code>visual/</code>, and <code>music/</code>.</p>
