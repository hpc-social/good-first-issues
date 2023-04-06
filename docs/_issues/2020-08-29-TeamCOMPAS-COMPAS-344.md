---
tags: ,enhancement,severity_minor,urgency_low
title: "Check for L2 overflow"
html_url: "https://github.com/TeamCOMPAS/COMPAS/issues/344"
user: ilyamandel
repo: TeamCOMPAS/COMPAS
---

Currently, we check whether stars are touching (e.g., left touching by an MT episode), and use this as a proxy for merger.  This check resolves to a check for whether the sum of the stellar radii exceeds the semi-major axis:

BaseBinaryStar.h:    bool                HasStarsTouching() const                    { return (utils::Compare(m_SemiMajorAxis, 0.0) > 0) && (m_SemiMajorAxis <= RSOL_TO_AU * (m_Star1->Radius() + m_Star2->Radius())); }

A more realistic check would consider whether stars engage in L2 overflow.  The two are equivalent for equal-mass stars in a circular binary, so the current check is not a terrible proxy, but we should improve this.

P.S. Should also address the initial check in the constructor of BaseBinaryStar (see #309 ).